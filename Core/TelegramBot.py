import os
import re
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN") or "")
dp = Dispatcher()

active_attacks = {}

# Настройки пользователя (тип атаки)
user_settings = {}

# Клавиатура с кнопками команд
def main_keyboard():
    kb = [
        [KeyboardButton(text="💣 Атака"), KeyboardButton(text="⏹ Стоп")],
        [KeyboardButton(text="📱 SMS"), KeyboardButton(text="📞 Звонки"), KeyboardButton(text="🔀 MIX")],
        [KeyboardButton(text="📖 Помощь"), KeyboardButton(text="ℹ️ О проекте")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def get_attack_type(user_id):
    return user_settings.get(user_id, "MIX")

def set_attack_type(user_id, atype):
    user_settings[user_id] = atype

@dp.message(Command("start"))
async def start_command(message: types.Message):
    uid = message.from_user.id
    atype = get_attack_type(uid)
    await message.answer(
        f"💣 **Добро пожаловать в Grobovsheke-SmsBomber!**\n\n"
        f"Используй кнопки ниже или команды:\n"
        f"• 💣 Атака — запустить атаку\n"
        f"• ⏹ Стоп — остановить\n"
        f"• 📖 Помощь — справка\n\n"
        f"⚙️ Текущий тип атаки: **{atype}**\n"
        f"📱 SMS — только сообщения\n"
        f"📞 Звонки — только звонки\n"
        f"🔀 MIX — всё сразу\n\n"
        "⚠️ Только в образовательных целях!",
        reply_markup=main_keyboard()
    )

@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(
        "📖 **Справка**\n\n"
        "▪️ Нажми **💣 Атака** и введи номер и время атаки\n"
        "▪️ Пример: `79123456789 5` (5 минут)\n"
        "▪️ Нажми **⏹ Стоп** чтобы остановить\n\n"
        "Время атаки: от 1 до 10 минут"
    )

@dp.message(Command("attack"))
async def attack_command(message: types.Message):
    user_id = message.from_user.id
    args = message.text.split()
    if len(args) < 3:
        await message.answer(
            "❌ Введи номер и время атаки в минутах.\n"
            "Пример: `/attack 79123456789 5`\n"
            "Или просто напиши: `79123456789 5`"
        )
        return
    await run_attack(message, args[1], args[2])

async def run_attack(message: types.Message, number: str, minutes: str):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if not number.isdigit() or not minutes.isdigit():
        await message.answer("❌ Номер и время должны быть числами!")
        return
    mins = int(minutes)
    if mins < 1 or mins > 10:
        await message.answer("❌ Время атаки от 1 до 10 минут!")
        return

    # Останавливаем предыдущую атаку пользователя если была
    if user_id in active_attacks and active_attacks[user_id]["status"] == "running":
        try:
            from Core.Run import stop_attacks
            stop_attacks()
        except:
            pass

    attack_type = get_attack_type(user_id)
    from Core.Run import start_async_attacks
    from threading import Thread
    import asyncio
    import time

    attack_id = int(time.time() * 1000)
    active_attacks[user_id] = {"number": number, "minutes": minutes, "status": "running", "type": attack_type, "id": attack_id}

    def run(aid):
        try:
            start_async_attacks(number, minutes, attack_type=attack_type, stop_previous=True)
            # Проверяем, не запустили ли новую атаку
            current = active_attacks.get(user_id, {})
            if current.get("id") != aid:
                return
            if current.get("status") == "stopped":
                return
            active_attacks[user_id]["status"] = "completed"
            asyncio.run(bot.send_message(
                chat_id,
                f"✅ **Атака завершена!**\n\n"
                f"📱 Номер: `{number}`\n"
                f"⏱ Длительность: `{minutes} мин.`\n"
                f"🔀 Тип: {attack_type}\n"
                f"📊 Статус: ✅ Выполнено",
                parse_mode="Markdown"
            ))
        except Exception as e:
            current = active_attacks.get(user_id, {})
            if current.get("id") != aid:
                return
            active_attacks[user_id]["status"] = "error"
            try:
                asyncio.run(bot.send_message(
                    chat_id,
                    f"❌ **Ошибка при выполнении атаки:**\n`{e}`",
                    parse_mode="Markdown"
                ))
            except:
                pass

    Thread(target=run, args=(attack_id,), daemon=True).start()

    await message.answer(
        f"✅ **Атака запущена!**\n📱 Номер: `{number}`\n⏱ Длительность: `{minutes} мин.`\n🔀 Тип: {attack_type}\n💣 Сообщения идут непрерывно...",
        reply_markup=main_keyboard()
    )

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

# Обработка текстовых сообщений (кнопки)
@dp.message()
async def handle_text(message: types.Message):
    text = message.text.strip()
    uid = message.from_user.id
    if text == "💣 Атака":
        atype = get_attack_type(uid)
        await message.answer(
            f"Введи номер и время атаки в минутах через пробел:\n"
            f"Пример: \`79123456789 5\` (5 минут)\n\n"
            f"⚙️ Текущий тип: {atype}\n"
            f"Можешь сменить кнопками ниже 👇"
        )
    elif text in ("📱 SMS", "📞 Звонки", "🔀 MIX"):
        type_map = {"📱 SMS": "SMS", "📞 Звонки": "CALL", "🔀 MIX": "MIX"}
        atype = type_map[text]
        set_attack_type(uid, atype)
        await message.answer(f"✅ Тип атаки изменён на **{atype}**", reply_markup=main_keyboard())
    elif text == "⏹ Стоп":
        await stop_command(message)
    elif text == "📖 Помощь":
        await help_command(message)
    elif text == "ℹ️ О проекте":
        await start_command(message)
    else:
        # Проверяем, не ввёл ли пользователь номер и время
        parts = text.split()
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            await run_attack(message, parts[0], parts[1])
        else:
            await message.answer(
                "Используй кнопки ниже 👇 или команды:\n"
                "/attack <номер> <минуты>\n/stop\n/help",
                reply_markup=main_keyboard()
            )

async def start_telegram_bot():
    await dp.start_polling(bot, handle_signals=False)
