from aiogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove
#from web.database import Database


def fao_keyboard() -> InlineKeyboardMarkup: 
    keyboard = InlineKeyboardMarkup()
    fao = Database.Fao()
    for i in range(0, len(fao)):
        button = InlineKeyboardButton(text = fao.keys[i], callback_data=f"fao_btn{i}")
        keyboard.add(button)
    return keyboard

def mute_keyboard(count:int = 0) -> InlineKeyboardMarkup: 
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text = f"{count}", callback_data=f"mute{count}"))
    return keyboard

def welcome_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text = "Нажми на клавишу в течении 60 секунд.", callback_data=f"welcome"))
    return keyboard
