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


@dispatcher.message_handler(commands="mute", commands_prefix="/")
async def mute_command(message: types.Message):
    if not message.reply_to_message:
        reply = await message.reply(text="Нужен реплай на сообщение пользователя!")
        await asyncio.sleep(10)
        await message.bot.delete_message(chat_id=message.chat.id, message_id=reply.message_id)
    else:
        warns = check_warns(message.reply_to_message.from_user.id)
        mute_time = warns * 10 + (warns - 1) * 10
        reply = await message.reply_poll(question=f"Замутить этого пользователя: id:{message.reply_to_message.from_user.id} Имя:{message.reply_to_message.from_user.first_name}?",
        is_anonymous=False, open_period=60, reply_to_message_id=message.reply_to_message.message_id, allow_sending_without_reply=True)



@dispatcher.poll_handler()


@dispatcher.message_handler(commands="fao", commands_prefix="/")
async def fao_command(message: types.Message):
    text = "text"
    markup = fao_keyboard()
    message.reply(text=text, reply_markup=markup)