from aiogram import types
from loader import dp
from dataBase.base import add_last_message


@dp.message_handler()
async def all_message(message: types.Message):
    add_last_message(message.chat.id)
    await message.answer("🤷 Я не понимаю")