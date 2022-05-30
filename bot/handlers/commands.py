import asyncio
from time import time
from aiogram import types, exceptions
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


from dispatcher import dispatcher
from .keyboards import fao_keyboard
from .functions import check_warns


class FSM(StatesGroup):
    user_id = State
    text = State


@dispatcher.message_handler(commands="start", commands_prefix="/")
async def start_command(message: types.Message):
    if message.chat.type =="private":
        message.bot.send_message(chat_id=message.from_user.id,
        text = "start text", parse_mode="HTML")
    else: return


@dp.message_handler(commands= ["mute"], commands_prefix="/")
async def mute(message: types.Message):
	if message.reply_to_message is not None:
		await message.bot.send_poll(chat_id=message.chat.id, question=f"Выдать мут пользователю id: {message.reply_to_message.from_user.id}", 
		options =['+', '-'], reply_to_message_id=message.reply_to_message.message_id, is_anonymous=False)
	else:
		message.reply("Нужен реплай на сообщение!")


# @dp.poll_handler()
# async def poll_handler(poll:types.Poll):
# 	print(poll)
# 	if poll["options"]["voter_count"] == 10:
# 		time = 
# 		restrict_id=re.findall("(\d+)",poll["question"])
# 		await bot.stop_poll(chat_id=chat_id,message_id=message_id)
# 		await bot.restrict_chat_member(chat_id=chat_id, user_id=restrict_id, permissions =types.ChatPermissions(False), until_date = time)



@dispatcher.message_handler(commands="fao", commands_prefix="/")
async def fao_command(message: types.Message):
    text = "text"
    markup = fao_keyboard()
    message.reply(text=text, reply_markup=markup)