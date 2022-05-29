from dis import dis
from aiogram import types

from dispatcher import dispatcher, bot
from web.database import Database


@dispatcher.callback_query_handler(lambda c: c.data and c.data.startswith('fao_btn'))
async def callback_fao(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        fao = Database.Fao()#.get_fao()
        await bot.answer_callback_query(callback_query.id)
        text = fao.keys[int(code)]
    else:
        text = "Error, i dont find this article!"
    await callback_query.message.edit_text(callback_query.from_user.id, text = text, reply_markup='')