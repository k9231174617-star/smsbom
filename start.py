import os
import asyncio
from Core.Main import Start
from Core.TelegramBot import start_telegram_bot

async def main():
    # Получаем порт из переменной окружения Railway
    port = int(os.environ.get("PORT", 9876))

    # Запускаем Telegram-бота в фоне
    telegram_task = asyncio.create_task(start_telegram_bot())

    # Запускаем веб-интерфейс
    Start(web=True, port=port)

    # Ждём завершения работы Telegram-бота (это никогда не произойдёт, пока бот работает)
    await telegram_task

if __name__ == "__main__":
    asyncio.run(main())