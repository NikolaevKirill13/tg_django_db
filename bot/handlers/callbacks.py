from itertools import count
import json
from aiogram import types
from dispatcher import dispatcher, bot
#from web.database import Database
from handlers import keyboards


@dispatcher.callback_query_handler(lambda c: c.data and c.data.startswith('fao_btn'))
async def callback_fao(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        fao #= Database.Fao()#.get_fao()
        await bot.answer_callback_query(callback_query.id)
        text = fao.keys[int(code)]
    else:
        text = "Error, i dont find this article!"
    await callback_query.message.edit_text(callback_query.from_user.id, text = text, reply_markup='')


#mute callback, dont work
#@dispatcher.callback_query_handler(lambda c: c.data and c.data.startswith('mute_btn'))
#async def callback_mute(callback_query: types.CallbackQuery):
#    code = callback_query.data[-1]
#    print(callback_query)
#    await bot.answer_callback_query(callback_query.id)
#    await callback_query.message.edit_reply_markup(reply_markup=keyboards.mute_keyboard(code))

@dispatcher.callback_query_handler(lambda c: c.data and c.data.startswith('mute'))
async def mute_callback_button(callback_query: types.CallbackQuery):
    #problems with callback_query
    print(callback_query.as_json().find("text"))
    await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=keyboards.mute_keyboard())
