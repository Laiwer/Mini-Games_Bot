from aiogram import types
from loader import dp
from dataBase.base import add_last_message


@dp.callback_query_handler(text="Одинаковые по цвету")
async def main_menu(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer(text="\"🎨 Одинаковые по цвету\" находиться в разработке...", show_alert=True)