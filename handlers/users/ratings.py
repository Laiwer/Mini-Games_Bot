from aiogram import types
from loader import dp
from dataBase.base import get_player_from_user_id, \
    get_all_record_search_emoji_small_from_player, get_all_record_search_emoji_medium_from_player, \
    get_all_record_search_emoji_hard_from_player, add_last_message, get_all_count_referal_from_player, \
    get_all_trophies_from_player, get_all_record_connect_in_order_from_player
from keyboards.inline.all_ratings import all_ratings_keyboard, \
    mini_games_rating_keyboard, \
    record_search_emoji_small_rating_keyboard_top, record_search_emoji_small_rating_keyboard_near, \
    record_search_emoji_medium_rating_keyboard_top, record_search_emoji_medium_rating_keyboard_near, \
    record_search_emoji_hard_rating_keyboard_top, record_search_emoji_hard_rating_keyboard_near, \
    mini_game_record_search_emoji_rating_keyboard, count_referal_rating_keyboard_top, \
    count_referal_rating_keyboard_near, trophies_rating_keyboard_top, trophies_rating_keyboard_near, \
    record_connect_in_order_keyboard_top, record_connect_in_order_keyboard_near
from keyboards.inline.callback_back_page import back_page_callback
from keyboards.inline.callback_ratings import ratings_callback


@dp.message_handler(text="🏆 Рейтинг")
async def choice_ratings(message: types.Message):
    add_last_message(message.chat.id)
    await message.answer("Выбери один из рейтингов:", reply_markup=all_ratings_keyboard)


@dp.callback_query_handler(back_page_callback.filter(page="ratings"))
async def back_to_all_ratings(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    await call.message.edit_text("Выбери один из рейтингов:", reply_markup=all_ratings_keyboard)


@dp.callback_query_handler(back_page_callback.filter(page="ratings_mini_games"))
async def back_to_all_rating_mini_game(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await rating_mini_games(call)



#!    Top trophies
@dp.callback_query_handler(text="Всего трофеев")
async def all_count_trophies(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    msg = show_first_five_lider("🏆 Рейтинг по количеству трофеев", get_all_trophies_from_player(), call.message.chat.id, after_place=" 🏆")
    try:
        await call.message.edit_text(msg, reply_markup=trophies_rating_keyboard_near)
    except Exception: pass


@dp.callback_query_handler(ratings_callback.filter(form="top", top="trophies"))
async def show_rating_all_count_trophies_top(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    try:
        await all_count_trophies(call)
    except Exception: pass


@dp.callback_query_handler(ratings_callback.filter(form="you", top="trophies"))
async def show_rating_all_count_trophies_player(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    msg = show_players_near_player("🏆 Рейтинг по количеству трофеев", get_all_trophies_from_player(), call.message.chat.id, after_place=" 🏆")
    try:
        await call.message.edit_text(msg, reply_markup=trophies_rating_keyboard_top)
    except Exception: pass



#!    Top count referal
@dp.callback_query_handler(text="Количество рефералов")
async def rating_count_referal(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    msg = show_first_five_lider("👥 Рейтинг по количествам рефералов", get_all_count_referal_from_player(), call.message.chat.id, after_place=" чел.")
    try:
        await call.message.edit_text(msg, reply_markup=count_referal_rating_keyboard_near)
    except Exception: pass


@dp.callback_query_handler(ratings_callback.filter(form="top", top="count_referal"))
async def show_rating_count_referal_top(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    try:
        await rating_count_referal(call)
    except Exception: pass


@dp.callback_query_handler(ratings_callback.filter(form="you", top="count_referal"))
async def show_rating_count_referal_player(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    msg = show_players_near_player("👥 Рейтинг по количествам рефералов", get_all_count_referal_from_player(), call.message.chat.id, after_place=" чел.")
    try:
        await call.message.edit_text(msg, reply_markup=count_referal_rating_keyboard_top)
    except Exception: pass



#!    Top mini games
@dp.callback_query_handler(text="rating_mini_games")
async def rating_mini_games(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    await call.message.edit_text("Выбери мини-игру: 🔽", reply_markup=mini_games_rating_keyboard)


@dp.callback_query_handler(text="record_search_emoji")
async def rating_mini_game_record_search_emoji(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    await call.message.edit_text("Выбери размер поля:", reply_markup=mini_game_record_search_emoji_rating_keyboard)


@dp.callback_query_handler(text="ratings_mini_games_size")
async def rating_mini_game_record_searc_emoji_size(call: types.CallbackQuery):
    await rating_mini_game_record_search_emoji(call)



#!    Top connect in order
@dp.callback_query_handler(text="record_connect_in_order")
async def rating_mg_connect_in_order(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    msg = show_first_five_lider("#️⃣🏆 Рейтинг по пройденным играм в \"🔢 Соединить по порядку\"", get_all_record_connect_in_order_from_player(), call.message.chat.id, after_place=" игр.")
    try:
        await call.message.edit_text(msg, reply_markup=record_connect_in_order_keyboard_near)
    except Exception: pass


@dp.callback_query_handler(ratings_callback.filter(form="top", top="connect_in_order"))
async def show_rating_connect_in_order_record_top(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    try:
        await rating_mg_connect_in_order(call)
    except Exception: pass


@dp.callback_query_handler(ratings_callback.filter(form="you", top="connect_in_order"))
async def show_rating_connect_in_order_record_player(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    msg = show_players_near_player("#️⃣🏆 Рейтинг по пройденным играм в \"🔢 Соединить по порядку\"", get_all_record_connect_in_order_from_player(), call.message.chat.id, after_place=" игр.")
    try:
        await call.message.edit_text(msg, reply_markup=record_connect_in_order_keyboard_top)
    except Exception: pass



#!    Top search emoji record 3x3
@dp.callback_query_handler(text="record_3x3")
async def rating_search_emoji_record_3x3(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    msg = show_first_five_lider("▫️🏆 Рекорды в \"🔎 Найди эмодзи\" 3 x 3", get_all_record_search_emoji_small_from_player(), call.message.chat.id, before_place="этап ")
    try:
        await call.message.edit_text(msg, reply_markup=record_search_emoji_small_rating_keyboard_near)
    except Exception: pass


@dp.callback_query_handler(ratings_callback.filter(form="top", top="r_search_e_small"))
async def show_rating_search_emoji_record_3x3_top(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    try:
        await rating_search_emoji_record_3x3(call)
    except Exception: pass


@dp.callback_query_handler(ratings_callback.filter(form="you", top="r_search_e_small"))
async def show_rating_search_emoji_record_3x3_player(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    msg = show_players_near_player("▫️🏆 Рекорды в \"🔎 Найди эмодзи\" 3 x 3", get_all_record_search_emoji_small_from_player(), call.message.chat.id, before_place="этап ")
    try:
        await call.message.edit_text(msg, reply_markup=record_search_emoji_small_rating_keyboard_top)
    except Exception: pass


#!    Top search emoji record 5x5
@dp.callback_query_handler(text="record_5x5")
async def rating_search_emoji_record_5x5(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    msg = show_first_five_lider("◽️🏆 Рекорды в \"🔎 Найди эмодзи\" 5 x 5", get_all_record_search_emoji_medium_from_player(), call.message.chat.id, before_place="этап ")
    try:
        await call.message.edit_text(msg, reply_markup=record_search_emoji_medium_rating_keyboard_near)
    except Exception: pass


@dp.callback_query_handler(ratings_callback.filter(form="top", top="r_search_e_medium"))
async def show_rating_search_emoji_record_5x5_top(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    try:
        await rating_search_emoji_record_5x5(call)
    except Exception: pass


@dp.callback_query_handler(ratings_callback.filter(form="you", top="r_search_e_medium"))
async def show_rating_search_emoji_record_5x5_player(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    msg = show_players_near_player("◽️🏆 Рекорды в \"🔎 Найди эмодзи\" 5 x 5", get_all_record_search_emoji_medium_from_player(), call.message.chat.id, before_place="этап ")
    try:
        await call.message.edit_text(msg, reply_markup=record_search_emoji_medium_rating_keyboard_top)
    except Exception: pass


#!    Top search emoji record 7x7
@dp.callback_query_handler(text="record_7x7")
async def rating_search_emoji_record_7x7(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    msg = show_first_five_lider("◻️🏆 Рекорды в \"🔎 Найди эмодзи\" 7 x 7", get_all_record_search_emoji_hard_from_player(), call.message.chat.id, before_place="этап ")
    try:
        await call.message.edit_text(msg, reply_markup=record_search_emoji_hard_rating_keyboard_near)
    except Exception: pass


@dp.callback_query_handler(ratings_callback.filter(form="top", top="r_search_e_hard"))
async def show_rating_search_emoji_record_7x7_top(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    try:
        await rating_search_emoji_record_7x7(call)
    except Exception: pass


@dp.callback_query_handler(ratings_callback.filter(form="you", top="r_search_e_hard"))
async def show_rating_search_emoji_record_7x7_player(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    msg = show_players_near_player("◻️🏆 Рекорды в \"🔎 Найди эмодзи\" 7 x 7", get_all_record_search_emoji_hard_from_player(), call.message.chat.id, before_place="этап ")
    try:
        await call.message.edit_text(msg, reply_markup=record_search_emoji_hard_rating_keyboard_top)
    except Exception: pass


# function for show top
def show_first_five_lider(name_top:str, top:dict, user_id:int, after_place:str="", multy:int=1, before_place:str="") -> str:
    msg = f"{name_top}\n--------------------------------------------\n"
    msg += "Пятёрка лидеров:\n"
    key_top = sorted(top, key=top.get, reverse=True)
    for i, v in enumerate(key_top):
        tmp1 = f"{int(top[v])*multy:,}"
        player = f"<b><i>{get_player_from_user_id(v)}</i></b>" if int(v) == int(user_id) else get_player_from_user_id(v)
        if i == 0:
            msg += f"🥇 {player} • {before_place}{tmp1}{after_place}\n"
        elif i == 1:
            msg += f"🥈 {player} • {before_place}{tmp1}{after_place}\n"
        elif i == 2:
            msg += f"🥉 {player} • {before_place}{tmp1}{after_place}\n"
        elif i == 3:
            msg += f" ➍ {player} • {before_place}{tmp1}{after_place}\n"
        elif i == 4:
            msg += f" ➎ {player} • {before_place}{tmp1}{after_place}\n"
    return msg


def show_players_near_player(name_top:str, top:dict, user_id:int, after_place:str="", multy:int=1, before_place:str="") -> str:
    msg = f"{name_top}\n--------------------------------------------\n"
    msg += "Игроки около вас:\n"
    key_top = sorted(top, key=top.get, reverse=True)
    for i in range(len(key_top)):
        if int(key_top[i]) == int(user_id):
            if i >= 3: msg += ".......\n"
            i__, i_, i_1, i_2, i_3 = f"{i-1}.", f"{i}.", f"{i+1}.", f"{i+2}.", f"{i+3}."
            if i_1 == "7.":
                i__ = " ➎"
            elif i_1 == "6.":
                i__ = " ➍"
                i_ = " ➎"
            elif i_1 == "5.":
                i__ = "🥉 "
                i_ = " ➍"
                i_1 = " ➎"
            elif i_1 == "4.":
                i__ = "🥈 "
                i_ = "🥉 "
                i_1 = " ➍"
                i_2 = " ➎"
            elif i_1 == "3.":
                i__ = "🥇 "
                i_ = "🥈 "
                i_1 = "🥉 "
                i_2 = " ➍"
                i_3 = " ➎"
            elif i_1 == "2.":
                i_ = "🥇 "
                i_1 = "🥈 "
                i_2 = "🥉 "
                i_3 = " ➍"
            elif i_1 == "1.":
                i_1 = "🥇 "
                i_2 = "🥈 "
                i_3 = "🥉 "
            try:
                if i not in [0, 1]:
                    msg += f"{i__} {get_player_from_user_id(key_top[i-2])} • {before_place}{int(top[key_top[i-2]])*multy:,}{after_place}\n"
                if i != 0:
                    msg += f"{i_} {get_player_from_user_id(key_top[i-1])} • {before_place}{int(top[key_top[i-1]])*multy:,}{after_place}\n"
                msg += f"{i_1} <b><i>{get_player_from_user_id(key_top[i])} • {before_place}{int(top[key_top[i]])*multy:,}{after_place}</i></b>\n"
                msg += f"{i_2} {get_player_from_user_id(key_top[i+1])} • {before_place}{int(top[key_top[i+1]])*multy:,}{after_place}\n"
                msg += f"{i_3} {get_player_from_user_id(key_top[i+2])} • {before_place}{int(top[key_top[i+2]])*multy:,}{after_place}\n"
            except Exception:
                pass
            if i <= len(key_top)-4: msg += "......."
    return msg
