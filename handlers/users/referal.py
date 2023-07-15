from aiogram import types
from loader import dp
from dataBase.base import count_referal


@dp.message_handler(text="👥 Рефералы")
async def show_referal(message: types.Message):
    msg = f"👥 Ваше количество рефералов: <b>{count_referal(message.from_user.id)} чел.</b>"
    msg += f"\n💭 Ваша реферальная ссылка:\nhttps://t.me/play_mini_games_bot?start={message.from_user.id}"
    await message.answer(msg)