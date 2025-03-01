import os
from telethon.sync import TelegramClient
from telethon import events
from datetime import datetime

# Читаем данные из переменных окружения
api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")
username = os.getenv("TELEGRAM_USERNAME")
target_chat_id = int(os.getenv("TARGET_CHAT_ID"))

# Создаём клиента Telegram
client = TelegramClient(username, api_id, api_hash, system_version="4.16.30-vxCUSTOM")

@client.on(events.NewMessage)
async def handler(event):
    """Обработчик новых сообщений — выводит их в логи"""
    if event.chat_id == target_chat_id:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"[{timestamp}] Новое сообщение: {event.message.text}"
        
        # Выводим сообщение в логи Railway
        print(log_message)

async def main():
    print(f"Отслеживание новых сообщений для чата/канала с ID {target_chat_id}...")
    await client.start()
    await client.run_until_disconnected()  # Держим бота в онлайне

with client:
    client.loop.run_until_complete(main())
