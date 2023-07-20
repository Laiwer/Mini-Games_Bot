from aiogram import types
from loader import dp
from dataBase.base import add_last_message
import random
import asyncio
from data.emoji_for_connect_in_order import EMOJI
from keyboards.inline.callback_mg_connect_in_order import mg_connect_in_order_callback
from dataBase.base import update_now_number_connect_in_order, get_connect_in_order, update_win_connect_in_order, \
    increase_all_complite_game_connect_in_order, profit_by_search_emoji_on_field, increase_played_mini_games, \
    get_game_field_connect_in_order, update_game_field_connect_in_order
from keyboards.inline.mg_connect_in_order_kb import start_connect_in_order_keyboard, end_connect_in_order_keyboard
from keyboards.inline.choice_mini_games_kb import mini_games_keyboard


@dp.callback_query_handler(text="Соединить по порядку")
async def main_menu(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()

    msg = "🔢 <b>Соедините числа с 1️⃣ до 3️⃣6️⃣</b>"
    msg += "\n🕰 Ваша игра не ограничена по времени"
    msg += "\n-------------------------------------------------"
    msg += "\n🤩 После прохождения вы получите <u>3🏆</u>"
    msg += "\n💥 <b>А если вам не удасться пройти, то вы потеряете <u>3🏆</u></b>"
    await call.message.edit_text(text=msg, reply_markup=start_connect_in_order_keyboard)


@dp.callback_query_handler(text="back_connect_in_order")
async def back_to_mini_games(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    await call.message.edit_text("Выбери мини-игру: ⤵", reply_markup=mini_games_keyboard)


@dp.callback_query_handler(text="end_connect_in_order")
async def end_play_connect_in_order(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    try:
        await main_menu(call)
    except Exception: pass


@dp.callback_query_handler(text="start_connect_in_order")
async def start_game_connect_in_order(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    increase_played_mini_games(call.message.chat.id)
    await call.answer()
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    random.shuffle(keys)

    update_game_field_connect_in_order(call.message.chat.id, keys)

    kb = types.InlineKeyboardMarkup(row_width=6)
    for i in get_game_field_connect_in_order(call.message.chat.id):
        kb.insert(types.InlineKeyboardButton(text=f"{EMOJI[i]}", callback_data=f"now_num:catch:{i}"))
    await call.message.edit_text(text=f"🔢 Найди: <b>{get_connect_in_order(call.message.chat.id)[0] + 1}</b>", reply_markup=kb)
    while True:
        try:
            data = get_connect_in_order(call.message.chat.id)
            if data[0] == 36 or data[1] == 0:
                break
            kb = types.InlineKeyboardMarkup(row_width=6)
            for i in get_game_field_connect_in_order(call.message.chat.id):
                kb.insert(types.InlineKeyboardButton(text=f"{EMOJI[i]}", callback_data=f"now_num:catch:{i}"))
            await call.message.edit_text(text=f"🔢 Найди: <b>{get_connect_in_order(call.message.chat.id)[0] + 1}</b>", reply_markup=kb)
        except Exception: pass


    if get_connect_in_order(call.message.chat.id)[0] == 36:
        await call.message.edit_text(text=f"🧐 Вы собрали все числа по порядку!\n🎉 Вы получаеelте <b><u>3</u></b>🏆", reply_markup=end_connect_in_order_keyboard)
        increase_all_complite_game_connect_in_order(call.message.chat.id)
        profit_by_search_emoji_on_field(call.message.chat.id, 3, "+")
    elif get_connect_in_order(call.message.chat.id)[1] == 0:
        await call.message.edit_text(text=f"🥱 Увы, у вас не получилось собрать последовательность\n🔻 Вы потеряли <b><u>3</u></b>🏆", reply_markup=end_connect_in_order_keyboard)
        profit_by_search_emoji_on_field(call.message.chat.id, 3, "-")
    update_win_connect_in_order(call.message.chat.id, 1)
    update_now_number_connect_in_order(call.message.chat.id, 0)


@dp.callback_query_handler(mg_connect_in_order_callback.filter(pos="catch"))
async def update_now_number_in_mini_game(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)

    now_num = get_connect_in_order(call.message.chat.id)[0]
    if int(call.data[14:]) - 1 == now_num:
        update_now_number_connect_in_order(call.message.chat.id, call.data[14:])
        try:
            kb = types.InlineKeyboardMarkup(row_width=6)
            for i in get_game_field_connect_in_order(call.message.chat.id):
                kb.insert(types.InlineKeyboardButton(text=f"{EMOJI[i]}", callback_data=f"now_num:catch:{i}"))
            await call.message.edit_text(text=f"🔢 Найди: <b>{get_connect_in_order(call.message.chat.id)[0] + 1}</b>", reply_markup=kb)
        except Exception: pass
    elif int(call.data[14:]) == now_num:
        await call.answer(f"Вы уже нажали на {EMOJI[now_num]}!", show_alert=True)
    else:
        await call.answer()
        update_win_connect_in_order(call.message.chat.id, 0)