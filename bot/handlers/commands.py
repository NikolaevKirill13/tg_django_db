from aiogram import types

from dispatcher import dispatcher
from handlers import keyboards
#from handlers import functions


@dispatcher.message_handler(commands=["start"], commands_prefix="/")
async def start_command(message: types.Message):
    #if message.chat.type =="private":
        await message.bot.send_message(chat_id=message.chat.id,
        text = "start text", parse_mode="HTML")
    #else: return


@dispatcher.message_handler(commands= ["mute"], commands_prefix="/")
async def mute(message: types.Message):
    if message.reply_to_message is not None:
        await message.reply_to_message.reply(text=f"Выдать мут пользователю id: {message.reply_to_message.from_user.id}?", reply_markup=keyboards.mute_keyboard())
    else:
        await message.reply("Нужен реплай на сообщение!")


@dispatcher.message_handler(commands=["fao"], commands_prefix="/")
async def fao_command(message: types.Message):
    if message.chat.type !="private":
        return
    await message.bot.send_message(chat_id=message.chat.id, text="text", reply_markup=keyboards.fao_keyboard())