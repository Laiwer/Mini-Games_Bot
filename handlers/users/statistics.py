from aiogram import types
from loader import dp
from keyboards.inline.statistics_keyboard import all_statistics_keyboards, mini_games_statistics_keyboards, \
    back_from_mini_game_statistics_keyboard
from dataBase.base import add_last_message, count_all_bot_users, count_active_bot_users, count_recently_bot_users, \
    count_time_in_bot, get_search_emoji_on_field, existe_in_db, add_mini_game_search_emoji_on_field_in_data_base, \
    get_connect_in_order


@dp.message_handler(text="📊 Статистика")
async def show_all_statistics(message: types.Message):
    add_last_message(message.chat.id)
    msg = "📊 <b><u>Общая статистика</u></b>"
    msg += f"\n\n👨‍👨‍👦‍👦 Всего игроков: <b><i>{count_all_bot_users()} чел.</i></b>"
    msg += f"\n☀️ Играли не более суток назад: <b><i>{count_active_bot_users()} чел.</i></b>"
    msg += f"\n🕐 Играли не более часа назад: <b><i>{count_recently_bot_users()} чел.</i></b>"
    await message.answer(msg, reply_markup=all_statistics_keyboards)


@dp.callback_query_handler(text="Статистика мини-игр")
async def show_mini_games(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    msg = "Выбирете мини-игру: ⬇"
    try:
        await call.message.edit_text(msg, reply_markup=mini_games_statistics_keyboards)
    except Exception: pass


@dp.callback_query_handler(text="stata_search_emoji")
async def show_search_emoji_statistics(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    tab = "\t" * 2
    data = get_search_emoji_on_field(call.message.chat.id)
    msg = "\n🔎 <b><u>Найди эмодзи</u></b>"
    msg += "\n\n🏆 <b>Рекорд игры с размером поля</b>"
    msg += f"\n{tab}{tab}▫️3 на 3: <b><i>этап {data[3]}</i></b>"
    msg += f"\n{tab}{tab}◽️5 на 5: <b><i>этап {data[4]}</i></b>"
    msg += f"\n{tab}{tab}◻️7 на 7: <b><i>этап {data[5]}</i></b>"
    msg += "\n🌐 <b>Всего пройденных с размером поля</b>"
    msg += f"\n{tab}{tab}▫️3 на 3: <b><i>{data[6]} этап.</i></b>"
    msg += f"\n{tab}{tab}◽️5 на 5: <b><i>{data[7]} этап.</i></b>"
    msg += f"\n{tab}{tab}◻️7 на 7: <b><i>{data[8]} этап.</i></b>"
    try:
        await call.message.edit_text(msg, reply_markup=back_from_mini_game_statistics_keyboard)
    except Exception: pass


@dp.callback_query_handler(text="stata_connect_in_order")
async def show_connect_in_order_statistics(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    msg = "🔢 <b><u>Соединить по порядку</u></b>"
    msg += f"\n\n<b>🕹 Количество правильных последовательностей: <i>{get_connect_in_order(call.message.chat.id)[2]} игр</i></b>"
    try:
        await call.message.edit_text(msg, reply_markup=back_from_mini_game_statistics_keyboard)
    except Exception: pass


@dp.callback_query_handler(text="back_to_mini_game_statistics")
async def back_to_minigames_statistics(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    try:
        await show_mini_games(call)
    except Exception: pass


@dp.callback_query_handler(text="back_to_statistics")
async def back_to_all_statistics(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    msg = "📊 <b><u>Общая статистика</u></b>"
    msg += f"\n\n👨‍👨‍👦‍👦 Всего игроков: <b><i>{count_all_bot_users()} чел.</i></b>"
    msg += f"\n☀️ Играли не более суток назад: <b><i>{count_active_bot_users()} чел.</i></b>"
    msg += f"\n🕐 Играли не более часа назад: <b><i>{count_recently_bot_users()} чел.</i></b>"
    try:
        await call.message.edit_text(msg, reply_markup=all_statistics_keyboards)
    except Exception: pass