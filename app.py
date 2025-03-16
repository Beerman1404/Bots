import os

#from dotenv import load_dotenv

import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import LinkPreviewOptions
from aiogram.types import FSInputFile

from keyboards import choice_lang_kb, ru_kb, en_kb
from message_texts import ru_main_message, en_main_message, ru_proofs_message, en_proofs_message

# путь к .env файлу с переменными для библиотеки os
#dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
#if os.path.exists(dotenv_path):
#    load_dotenv(dotenv_path)

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)



# Объект бота
bot = Bot(token="7225610147:AAFWKvGAYvbHYybj1qpm1MRh8lpjErlcYPw",
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
)


# Диспетчер
dp = Dispatcher()


# Запуск процесса поллинга новых апдейтов
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Choose your language", reply_markup=choice_lang_kb)


## Русский вариант ##
@dp.message(F.text == "Russian")
async def ru_lang(message: types.Message):
    await message.answer(ru_main_message, link_preview_options=LinkPreviewOptions(url="https://t.me/tarantino_221"), reply_markup=ru_kb)

# хендлер для обработки кнопки ПРУФЫ/ОТЗЫВЫ
@dp.message(F.text == "❗️ ПРУФЫ/ОТЗЫВЫ ❗️")
async def ru_proofs(message: types.Message):
    await message.answer(ru_proofs_message)

# хендлер для обработки кнопки АДМИНИСТРАТОР
@dp.message(F.text == "❗️ АДМИНИСТРАТОР ❗️")
async def ru_admin(message: types.Message):
    await message.answer("❗️ АДМИНИСТРАТОР ❗️\n@tarantino_221", link_preview_options=LinkPreviewOptions(url="https://t.me/tarantino_221"))

# хендлер для обработки кнопки НАЗАД
@dp.message(F.text == "❗️ НАЗАД ❗️")
async def ru_back(message: types.Message):
    await message.answer("LANGUAGE MENU", reply_markup=choice_lang_kb)



## Английский вариант ##
@dp.message(F.text == "English")
async def en_lang(message: types.Message):
    await message.answer(en_main_message, link_preview_options=LinkPreviewOptions(url="https://t.me/tarantino_221"), reply_markup=en_kb)

# хендлер для обработки кнопки PROOFS/REVIEWS
@dp.message(F.text == "❗️ PROOFS/REVIEWS ❗️")
async def en_proofs(message: types.Message):
    await message.answer(en_proofs_message)

# хендлер для обработки кнопки ADMINISTRATOR
@dp.message(F.text == "❗️ ADMINISTRATOR ❗️")
async def en_admin(message: types.Message):
    await message.answer("❗️ ADMINISTRATOR ❗️\n@tarantino_221", link_preview_options=LinkPreviewOptions(url="https://t.me/tarantino_221"))

# хендлер для обработки кнопки BACK
@dp.message(F.text == "❗️ BACK ❗️")
async def en_back(message: types.Message):
    await message.answer("LANGUAGE MENU", reply_markup=choice_lang_kb)


@dp.message(F.text == "❗️ ПРОБНЫЕ ВИДЕО ❗️")
async def test_video(message: types.Message):
    video_from_pc = FSInputFile("videos/IMG_8558.MOV")
    await message.answer_video(video_from_pc, width=240, height=120)
    video_from_pc = FSInputFile("videos/IMG_8559.MOV")
    await message.answer_video(video_from_pc, width=120, height=240)
    video_from_pc = FSInputFile("videos/IMG_8560.MOV")
    await message.answer_video(video_from_pc, width=120, height=240)
    video_from_pc = FSInputFile("videos/IMG_8561.MOV")
    await message.answer_video(video_from_pc, width=120, height=240)
    video_from_pc = FSInputFile("videos/IMG_8562.MOV")
    await message.answer_video(video_from_pc, width=120, height=240)
    video_from_pc = FSInputFile("videos/IMG_8563.MOV")
    await message.answer_video(video_from_pc, width=120, height=240)
    video_from_pc = FSInputFile("videos/IMG_8564.MOV")
    await message.answer_video(video_from_pc, width=120, height=240)
    video_from_pc = FSInputFile("videos/IMG_8565.MOV")
    await message.answer_video(video_from_pc, width=120, height=240)
    video_from_pc = FSInputFile("videos/IMG_8567.MOV")
    await message.answer_video(video_from_pc, width=120, height=240)
    video_from_pc = FSInputFile("videos/IMG_8568.MOV")
    await message.answer_video(video_from_pc, width=240, height=120)

@dp.message(F.text == "❗️ TEST VIDEOS ❗️")
async def test_video(message: types.Message):
    video_from_pc = FSInputFile("videos/IMG_8558.MOV")
    await message.answer_video(video_from_pc, width=240, height=120)
    video_from_pc = FSInputFile("videos/IMG_8559.MOV")
    await message.answer_video(video_from_pc, width=120, height=240)
    video_from_pc = FSInputFile("videos/IMG_8560.MOV")
    await message.answer_video(video_from_pc, width=120, height=240)
    video_from_pc = FSInputFile("videos/IMG_8561.MOV")
    await message.answer_video(video_from_pc, width=120, height=240)
    video_from_pc = FSInputFile("videos/IMG_8562.MOV")
    await message.answer_video(video_from_pc, width=120, height=240)
    video_from_pc = FSInputFile("videos/IMG_8563.MOV")
    await message.answer_video(video_from_pc, width=120, height=240)
    video_from_pc = FSInputFile("videos/IMG_8564.MOV")
    await message.answer_video(video_from_pc, width=120, height=240)
    video_from_pc = FSInputFile("videos/IMG_8565.MOV")
    await message.answer_video(video_from_pc, width=120, height=240)
    video_from_pc = FSInputFile("videos/IMG_8567.MOV")
    await message.answer_video(video_from_pc, width=120, height=240)
    video_from_pc = FSInputFile("videos/IMG_8568.MOV")
    await message.answer_video(video_from_pc, width=240, height=120)

if __name__ == "__main__":
    asyncio.run(main())
