import os
import asyncio
import threading
from Core.Main import Start
from Core.TelegramBot import start_telegram_bot

def run_telegram_bot():
    """Run telegram bot in its own event loop in a thread"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_telegram_bot())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 9876))

    # Telegram bot в отдельном потоке (если есть токен)
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    if token:
        t = threading.Thread(target=run_telegram_bot, daemon=True)
        t.start()
    else:
        print("TELEGRAM_BOT_TOKEN не задан, Telegram бот не запущен")

    # Веб-интерфейс (Flet) — блокирующий вызов
    Start(web=True, port=port)
