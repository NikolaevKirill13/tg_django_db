from aiogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove
from web.database import Database


def fao_keyboard() -> InlineKeyboardMarkup: 
    keyboard = InlineKeyboardMarkup()
    fao = Database.Fao()#.get_fao()
    for i in range(0, len(fao)):
        button = InlineKeyboardButton(text = fao.keys[i], callback_data=f"fao_btn{i}")
        keyboard.add(button)
    return keyboard