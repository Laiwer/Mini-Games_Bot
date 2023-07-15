from aiogram import types
from loader import dp
from random import randint
import asyncio
from dataBase.base import get_search_emoji_on_field, update_is_win_search_emoji, add_mini_game_search_emoji_on_field_in_data_base, \
    existe_in_db, update_difficulty_search_emoji, update_stage_search_emoji, profit_by_search_emoji_on_field, get_data_from_player, \
    update_record_stage_and_all_stage_search_emoji, add_last_message
from keyboards.inline.choice_mini_games_kb import mini_games_keyboard   
from keyboards.inline.callback_back_page import back_page_callback
from keyboards.inline.mg_search_emoji_kb import size_field_keyboard, start_search_emoji_keyboard, continue_search_emoji_keyboard
from data.emoji_for_search_emoji_on_field import EMOJI



@dp.message_handler(text="🧩 Мини-игры")
async def choice_mini_games(message: types.Message):
    add_last_message(message.chat.id)
    if not existe_in_db("mini_game_search_emoji_on_field", message.chat.id):
        add_mini_game_search_emoji_on_field_in_data_base(message.chat.id)
    await message.answer("Выбери мини-игру: ⤵", reply_markup=mini_games_keyboard)



@dp.callback_query_handler(text="emoji")
async def searched_emoji_on_field(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    update_is_win_search_emoji(call.message.chat.id, 0)


@dp.callback_query_handler(text="wrong_emoji")
async def searched_emoji_on_field(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    update_is_win_search_emoji(call.message.chat.id, 2)


@dp.callback_query_handler(text="__emoji")
async def button_keyboard_after_search_emoji(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()


@dp.callback_query_handler(back_page_callback.filter(page="mini_games"))
async def go_back_to_choice_mini_games(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    await call.message.edit_text("Выбери мини-игру: ⤵", reply_markup=mini_games_keyboard)


@dp.callback_query_handler(text="Продолжить")
async def continue_play_search_emoji(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    data = get_search_emoji_on_field(call.message.chat.id)[1]
    if data == 3:
        await small_field(call)
    elif data == 5:
        await medium_field(call)
    elif data == 7:
        await hard_field(call)


@dp.callback_query_handler(text="Закончить")
async def end_play_search_emoji(call: types.CallbackQuery):
    await go_back_to_choice_mini_games(call)


@dp.callback_query_handler(text="Найди эмодзи")
async def search_emoji_on_field(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    await call.message.edit_text("Выберите сложность игры:", reply_markup=size_field_keyboard)


@dp.callback_query_handler(text="back_search_emoji_size")
async def back_to_size_search_emoji(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    try:
        await search_emoji_on_field(call)
    except Exception: pass


@dp.callback_query_handler(text="3x3")
async def small_field(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    update_difficulty_search_emoji(call.message.chat.id, 3)
    data = get_search_emoji_on_field(call.message.chat.id)
    stages = data[2]
    msg = f"💠 <b><u>Этап {stages}</u></b>"
    msg += "\n↕️ <b>Размер игрового поля: <u>3 x 3</u></b>"
    if stages == 1:
        msg += "\n-------------------------------------------------"
        msg += "\n⏱ Дано <b><i>3 секунды</i></b> чтобы посмотреть на эмодзи, который вам надо найти и <b><i>5 секунд</i></b> чтобы его найти"
        msg += "\n🎖 <b><u>Трофеи начисляются каждые пять этапов</u></b>"
        msg += "\n💥 <b><u>При проигрыше вы потеряете 5🏆</u></b>"
        await call.message.edit_text(msg, reply_markup=start_search_emoji_keyboard)
    elif stages >= 2:
        msg += "\n🏆 <b><i>Трофеи начисляются каждые пять этапов</i></b>"
        msg += "\n💢 <b><i>При проигрыше вы потеряете <u>5🏆</u></i></b>"
        await call.message.edit_text(msg, reply_markup=continue_search_emoji_keyboard)


@dp.callback_query_handler(text="5x5")
async def medium_field(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    update_difficulty_search_emoji(call.message.chat.id, 5)
    data = get_search_emoji_on_field(call.message.chat.id)
    stages = data[2]
    msg = f"💠 <b><u>Этап {stages}</u></b>"
    msg += "\n↕️ <b>Размер игрового поля: <u>5 x 5</u></b>"
    if stages == 1:
        msg += "\n-------------------------------------------------"
        msg += "\n⏱ Дано <b><i>3 секунды</i></b> чтобы посмотреть на эмодзи, который вам надо найти и <b><i>7 секунд</i></b> чтобы его найти"
        msg += "\n🎖 <b><u>Трофеи начисляются каждые пять этапов</u></b>"
        msg += "\n💥 <b><u>При проигрыше вы потеряете 3🏆</u></b>"
        await call.message.edit_text(msg, reply_markup=start_search_emoji_keyboard)
    elif stages >= 2:
        msg += "\n🏆 <b><i>Трофеи начисляются каждые пять этапов</i></b>"
        msg += "\n💢 <b><i>При проигрыше вы потеряете <u>3🏆</u></i></b>"
        await call.message.edit_text(msg, reply_markup=continue_search_emoji_keyboard)


@dp.callback_query_handler(text="7x7")
async def hard_field(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    update_difficulty_search_emoji(call.message.chat.id, 7)
    data = get_search_emoji_on_field(call.message.chat.id)
    stages = data[2]
    msg = f"💠 <b><u>Этап {stages}</u></b>"
    msg += "\n↕️ <b>Размер игрового поля: <u>7 x 7</u></b>"
    if stages == 1:
        msg += "\n-------------------------------------------------"
        msg += "\n⏱ Дано <b><i>3 секунды</i></b> чтобы посмотреть на эмодзи, который вам надо найти и <b><i>9 секунд</i></b> чтобы его найти"
        msg += "\n🎖 <b><u>Трофеи начисляются каждые пять этапов</u></b>"
        msg += "\n💥 <b><u>При проигрыше вы потеряете 1🏆</u></b>"
        await call.message.edit_text(msg, reply_markup=start_search_emoji_keyboard)
    elif stages >= 2:
        msg += "\n🏆 <b><i>Трофеи начисляются каждые пять этапов</i></b>"
        msg += "\n💢 <b><i>При проигрыше вы потеряете <u>1🏆</u></i></b>"
        await call.message.edit_text(msg, reply_markup=continue_search_emoji_keyboard)


@dp.callback_query_handler(text="Начать")
async def start_search_emoji_on_field(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    S = get_search_emoji_on_field(call.message.chat.id)[1]
    kb = types.InlineKeyboardMarkup(row_width=S)
    kb1 = types.InlineKeyboardMarkup(row_width=S)
    pos = 0
    pos_emoji = randint(0, S*S-1)
    choice_emoji = EMOJI[randint(0, len(EMOJI)-1)]
    for _ in range(S):
        for __ in range(S):
            if pos == pos_emoji:
                kb.insert(types.InlineKeyboardButton(text=choice_emoji[1], callback_data="emoji"))
                kb1.insert(types.InlineKeyboardButton(text=choice_emoji[1], callback_data="__emoji"))
            else:
                kb.insert(types.InlineKeyboardButton(text=choice_emoji[0], callback_data="wrong_emoji"))
                kb1.insert(types.InlineKeyboardButton(text="🫥", callback_data="__emoji"))
            pos += 1

    sec_start = 3
    await call.message.edit_text(text=f"⏳{sec_start}\nВам надо найти: {choice_emoji[1]}")
    for _ in range(3):
        await asyncio.sleep(1)
        sec_start -= 1
        await call.message.edit_text(text=f"⏳{sec_start}\nВам надо найти: {choice_emoji[1]}")

    SEC = [get_search_emoji_on_field(call.message.chat.id)[1]+2]
    sec, SEC = SEC[:][0], SEC[0]
    await call.message.edit_text(text=f"⏳{sec}\nНайдите: {choice_emoji[1]}", reply_markup=kb)
    for _ in range(SEC):
        if get_search_emoji_on_field(call.message.chat.id)[0] == 1:
            await asyncio.sleep(1)
            sec -= 1
            await call.message.edit_text(text=f"⏳{sec}\nНайдите: {choice_emoji[1]}", reply_markup=kb)
        if get_search_emoji_on_field(call.message.chat.id)[0] == 2:
            break

    if sec <= 0 or get_search_emoji_on_field(call.message.chat.id)[0] == 2:
        add_last_message(call.message.chat.id)
        kb1.insert(types.InlineKeyboardButton(text="⛔️ Закончить", callback_data="Закончить"))
        msg = f"😔 Проигрыш!\n🛑 Вы остановились на <b><u>этапе {get_search_emoji_on_field(call.message.chat.id)[2]-1}</u></b>\n📉 Вы потеряли <b><u>"
        data = get_search_emoji_on_field(call.message.chat.id)
        if data[1] == 3:
            profit_by_search_emoji_on_field(call.message.chat.id, 5, "-")
            msg += "5"
        elif data[1] == 5:
            profit_by_search_emoji_on_field(call.message.chat.id, 3, "-")
            msg += "3"
        elif data[1] == 7:
            profit_by_search_emoji_on_field(call.message.chat.id, 1, "-")
            msg += "1"
        msg += f"</u></b>🏆\n🔎 Вам надо было найти: {choice_emoji[1]}"
        await call.message.edit_text(msg, reply_markup=kb1)
        update_record_stage_and_all_stage_search_emoji(call.message.chat.id, get_search_emoji_on_field(call.message.chat.id)[1], get_search_emoji_on_field(call.message.chat.id)[2]-1)
        update_stage_search_emoji(call.message.chat.id, 1)
        update_is_win_search_emoji(call.message.chat.id, 1)
    else:
        add_last_message(call.message.chat.id)
        update_stage_search_emoji(call.message.chat.id)
        update_is_win_search_emoji(call.message.chat.id, 1)
        data = get_search_emoji_on_field(call.message.chat.id)
        msg = "🎉 Поздравляю!\n"
        if (data[2] - 1) % 5 == 0:
            msg += "👏 Вы заработали <b><u>"
            if data[1] == 3:
                profit_by_search_emoji_on_field(call.message.chat.id, 1, "+")
                msg += "1"
            elif data[1] == 5:
                profit_by_search_emoji_on_field(call.message.chat.id, 3, "+")
                msg += "3"
            elif data[1] == 7:
                profit_by_search_emoji_on_field(call.message.chat.id, 5, "+")
                msg += "5"
            msg += f"</u></b>🏆\n🔎 Вам надо было найти: {choice_emoji[1]}"
        else:
            msg += f"🔎 Вам надо было найти: {choice_emoji[1]}"
        kb1.insert(types.InlineKeyboardButton(text="⏩ Продолжить", callback_data="Продолжить"))
        await call.message.edit_text(msg, reply_markup=kb1)