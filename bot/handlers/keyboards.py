from tkinter import Button
from tkinter.messagebox import NO
from aiogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove
#from web.database import Database


def fao_keyboard() -> InlineKeyboardMarkup: 
    keyboard = InlineKeyboardMarkup()
    fao = Database.Fao()
    for i in range(0, len(fao)):
        button = InlineKeyboardButton(text = fao.keys[i], callback_data=f"fao_btn{i}")
        keyboard.add(button)
    return keyboard

def mute_keyboard(count:int = None) -> InlineKeyboardMarkup: 
    keyboard = InlineKeyboardMarkup()
    # if code is not None:
    #     if code == "1":
    #         keyboard.add(InlineKeyboardButton(text=f"За ", callback_data=="mute0"))
    #     keyboard.add()
    keyboard.add(InlineKeyboardButton(text = "0", callback_data="mute"))
    return keyboard