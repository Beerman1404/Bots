import os

from dotenv import load_dotenv

import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import LinkPreviewOptions
from aiogram.types import FSInputFile

from keyboards import choice_lang_kb, ru_kb, en_kb, en_gender_kb, ru_gender_kb, ru_boys_kb, en_boys_kb
from message_texts import ru_main_message, en_main_message, ru_proofs_message, en_proofs_message, boys_ru, boys_eng

load_dotenv()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)



# Объект бота
bot = Bot(token=os.getenv('TOKEN'),
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

@dp.message(F.text == "Russian")
async def ru_lang(message: types.Message):
    await message.answer("КТО ТЕБЯ ИНТЕРЕСУЕТ?", reply_markup=ru_gender_kb)

## Русский вариант ##
@dp.message(F.text == "❗️ ДЕВОЧКИ ❗️")
async def ru_girls(message: types.Message):
    await message.answer(ru_main_message, link_preview_options=LinkPreviewOptions(url="https://t.me/tarantino_221"), reply_markup=ru_kb)

@dp.message(F.text == "❗️ МАЛЬЧИКИ ❗️")
async def ru_boys(message: types.Message):
    await message.answer(boys_ru, link_preview_options=LinkPreviewOptions(url="https://t.me/tarantino_221"), reply_markup=ru_boys_kb)

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
    await message.answer("КТО ТЕБЯ ИНТЕРЕСУЕТ?", reply_markup=ru_gender_kb)



## Английский вариант ##
@dp.message(F.text == "English")
async def en_lang(message: types.Message):
    await message.answer("WHO INTERESTS YOU?", reply_markup=en_gender_kb)

@dp.message(F.text == "❗️ GIRLS ❗️")
async def en_female(message: types.Message):
    await message.answer(en_main_message, link_preview_options=LinkPreviewOptions(url="https://t.me/tarantino_221"), reply_markup=en_kb)

@dp.message(F.text == "❗️ BOYS ❗️")
async def en_boys(message: types.Message):
    await message.answer(boys_eng, link_preview_options=LinkPreviewOptions(url="https://t.me/tarantino_221"), reply_markup=en_boys_kb)

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
    await message.answer("WHO INTERESTS YOU?", reply_markup=en_gender_kb)


@dp.message(F.text == "❗️ ПРОБНЫЕ ВИДЕО ❗️")
async def test_video(message: types.Message):
    video_from_pc = FSInputFile("videos/IMG_1.MOV")
    await message.answer_video(video_from_pc, width=240, height=240)
    video_from_pc = FSInputFile("videos/IMG_2.MP4")
    await message.answer_video(video_from_pc, width=240, height=240)
    video_from_pc = FSInputFile("videos/IMG_3.MP4")
    await message.answer_video(video_from_pc, width=240, height=240)
    video_from_pc = FSInputFile("videos/IMG_4.MOV")
    await message.answer_video(video_from_pc, width=240, height=240)
    video_from_pc = FSInputFile("videos/IMG_5.MP4")
    await message.answer_video(video_from_pc, width=240, height=240)
        

@dp.message(F.text == "❗️ TEST VIDEOS ❗️")
async def test_video(message: types.Message):
    video_from_pc = FSInputFile("videos/IMG_1.MOV")
    await message.answer_video(video_from_pc, width=240, height=240)
    video_from_pc = FSInputFile("videos/IMG_2.MP4")
    await message.answer_video(video_from_pc, width=240, height=240)
    video_from_pc = FSInputFile("videos/IMG_3.MP4")
    await message.answer_video(video_from_pc, width=240, height=240)
    video_from_pc = FSInputFile("videos/IMG_4.MOV")
    await message.answer_video(video_from_pc, width=240, height=240)
    video_from_pc = FSInputFile("videos/IMG_5.MP4")
    await message.answer_video(video_from_pc, width=240, height=240)
        
if __name__ == "__main__":
    asyncio.run(main())
