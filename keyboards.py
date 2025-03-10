from aiogram import types

choice_lang_kb = types.ReplyKeyboardMarkup(
    keyboard=[
    [types.KeyboardButton(text="English"), types.KeyboardButton(text="Russian")]
    ], 
    resize_keyboard=True
)

ru_kb = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="❗️ ПРУФЫ/ОТЗЫВЫ ❗️")],
    [types.KeyboardButton(text="❗️ АДМИНИСТРАТОР ❗️")],
    [types.KeyboardButton(text="❗️ НАЗАД ❗️")]
    ], 
    resize_keyboard=True
)

en_kb = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="❗️ PROOFS/REVIEWS ❗️")],
    [types.KeyboardButton(text="❗️ ADMINISTRATOR ❗️")],
    [types.KeyboardButton(text="❗️ BACK ❗️")]
    ], 
    resize_keyboard=True
)
