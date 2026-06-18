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

# Клавиатура с кнопками команд
def main_keyboard():
    kb = [
        [KeyboardButton(text="💣 Атака"), KeyboardButton(text="⏹ Стоп")],
        [KeyboardButton(text="📖 Помощь"), KeyboardButton(text="ℹ️ О проекте")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(
        "💣 **Добро пожаловать в Grobovsheke-SmsBomber!**\n\n"
        "Используй кнопки ниже или команды:\n"
        "• 💣 Атака — запустить атаку\n"
        "• ⏹ Стоп — остановить\n"
        "• 📖 Помощь — справка\n\n"
        "⚠️ Только в образовательных целях!",
        reply_markup=main_keyboard()
    )

@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(
        "📖 **Справка**\n\n"
        "▪️ Нажми **💣 Атака** и введи номер с количеством повторов\n"
        "▪️ Пример: `79123456789 5`\n"
        "▪️ Нажми **⏹ Стоп** чтобы остановить\n\n"
        "Повторов: от 1 до 1000"
    )

@dp.message(Command("attack"))
async def attack_command(message: types.Message):
    user_id = message.from_user.id
    args = message.text.split()
    if len(args) < 3:
        await message.answer(
            "❌ Введи номер и количество повторов.\n"
            "Пример: `/attack 79123456789 5`\n"
            "Или просто напиши: `79123456789 5`"
        )
        return
    await run_attack(message, args[1], args[2])

async def run_attack(message: types.Message, number: str, replay: str):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if not number.isdigit() or not replay.isdigit():
        await message.answer("❌ Номер и повторы должны быть числами!")
        return
    if int(replay) < 1 or int(replay) > 1000:
        await message.answer("❌ Повторов от 1 до 1000!")
        return

    active_attacks[user_id] = {"number": number, "replay": replay, "status": "running"}

    from Core.Run import start_async_attacks
    from threading import Thread
    import asyncio

    def run():
        try:
            start_async_attacks(number, replay)
            if active_attacks.get(user_id, {}).get("status") == "stopped":
                return
            active_attacks[user_id]["status"] = "completed"
            asyncio.run(bot.send_message(
                chat_id,
                f"✅ **Атака завершена!**\n\n"
                f"📱 Номер: `{number}`\n"
                f"🔄 Повторов: `{replay}`\n"
                f"📊 Статус: ✅ Выполнено",
                parse_mode="Markdown"
            ))
        except Exception as e:
            active_attacks[user_id]["status"] = "error"
            try:
                asyncio.run(bot.send_message(
                    chat_id,
                    f"❌ **Ошибка при выполнении атаки:**\n`{e}`",
                    parse_mode="Markdown"
                ))
            except:
                pass

    Thread(target=run, daemon=True).start()

    await message.answer(
        f"✅ **Атака запущена!**\nНомер: `{number}`\nПовторов: `{replay}`",
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
    if text == "💣 Атака":
        await message.answer("Введи номер и количество повторов через пробел:\nПример: `79123456789 5`")
    elif text == "⏹ Стоп":
        await stop_command(message)
    elif text == "📖 Помощь":
        await help_command(message)
    elif text == "ℹ️ О проекте":
        await start_command(message)
    else:
        # Проверяем, не ввёл ли пользователь номер и повторы
        parts = text.split()
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            await run_attack(message, parts[0], parts[1])
        else:
            await message.answer(
                "Используй кнопки ниже 👇 или команды:\n"
                "/attack <номер> <повторы>\n/stop\n/help",
                reply_markup=main_keyboard()
            )

async def start_telegram_bot():
    await dp.start_polling(bot, handle_signals=False)
