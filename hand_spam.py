import os
from datetime import datetime, timedelta

from dotenv import load_dotenv

import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import LinkPreviewOptions
from aiogram.types import FSInputFile
from aiogram.types import InputMediaVideo
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.fsm.storage.memory import MemoryStorage

from models import SessionLocal, Users

logging.basicConfig(level=logging.INFO)

load_dotenv()
session = SessionLocal()

bot = Bot(token=os.getenv('TOKEN'),
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
)

# Диспетчер
dp = Dispatcher()

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


@dp.message(Command("spam"))
async def send_video(message: types.Message):
    users = session.query(Users.telegram_id).all()
    media_group = MediaGroupBuilder()

    for i in range(7):
        file_path = f"videos/spam/IMG_{i+1}.mp4"

        if not os.path.exists(file_path):
            print(f"❌ Файл не найден: {file_path}")
            continue

        file = FSInputFile(file_path)
        caption = "@FEETGIRLSOLES_BOT - ДОСТУП/ACCESS" if i == 0 else None

        media_group.add(
        type="video",
        media=file,
        caption=caption
        )
        
    for user in users:
        print("User : ", user.telegram_id)
        try:
                await bot.send_media_group(chat_id=user.telegram_id, media=media_group.build())
        except Exception as e:
            print(f'Ошибка отправки видео пользователю {user.telegram_id} {e}')
    print("Сообщения разосланы!")
    

if __name__ == "__main__":
    asyncio.run(main())