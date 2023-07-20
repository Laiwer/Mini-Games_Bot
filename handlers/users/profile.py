from aiogram import types
from loader import dp
from keyboards.inline.profile_setup import profile_keyboard
from keyboards.default.emoji_keyboard import emoji_choice_keyboard
from keyboards.default.main import main_keyboard
from states.update_emoji_player import update_emoji_profile_player
from aiogram.dispatcher.storage import FSMContext
from dataBase.base import update_emoji_player, add_last_message, get_data_from_player, count_time_in_bot
import emoji


@dp.message_handler(text="👤 Профиль")
async def my_profile(message: types.Message):
    add_last_message(message.chat.id)
    data = get_data_from_player(message.chat.id)
    msg = f"🔗 <b>ID:</b> {message.chat.id}"
    msg += f"\n🪪 <b>Никнейм:</b> {data[1]} {data[0]}"
    msg += "\n--------------------------------------"
    
    timee = count_time_in_bot(message.chat.id)
    if timee[0] == 0:
        if timee[1] == 0:
            msg += f"\n🕰 <b>Вы играете:</b> {timee[2]} ч. {0 if timee[3] < 0 else timee[3]} мин."
        else:
            msg += f"\n🕰 <b>Вы играете:</b> {timee[1]} дн. {timee[2]} ч."
    else:
        msg += f"\n🕰 <b>Вы играете:</b> {timee[0]} мес. {timee[1]} дн. {timee[2]} ч." #

    msg += f"\n🏆 <b>Трофеи:</b> {data[2]}"
    msg += f"\n🎮 <b>Сыграно всего мини-игр:</b> {data[3]}"
    await message.answer(msg, reply_markup=profile_keyboard)


@dp.callback_query_handler(text="Обновить профиль")
async def update_my_profile(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    data = get_data_from_player(call.message.chat.id)
    msg = f"🔗 <b>ID:</b> {call.message.chat.id}"
    msg += f"\n🪪 <b>Никнейм:</b> {data[1]} {data[0]}"
    msg += "\n--------------------------------------"
    
    timee = count_time_in_bot(call.message.chat.id)
    if timee[0] == 0:
        if timee[1] == 0:
            msg += f"\n🕰 <b>Вы играете:</b> {timee[2]} ч. {0 if timee[3] < 0 else timee[3]} мин."
        else:
            msg += f"\n🕰 <b>Вы играете:</b> {timee[1]} дн. {timee[2]} ч."
    else:
        msg += f"\n🕰 <b>Вы играете:</b> {timee[0]} мес. {timee[1]} дн. {timee[2]} ч."

    msg += f"\n🏆 <b>Трофеи:</b> {data[2]}"
    msg += f"\n🎮 <b>Сыграно всего мини-игр:</b> {data[3]}"
    try:
        await call.message.edit_text(msg, reply_markup=profile_keyboard)
    except Exception:
        pass


@dp.callback_query_handler(text="Поменять эмодзи")
async def update_player_emoji_1(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer()
    await call.message.answer("⏪ Введите эмодзи, который будет перед вашим ником: ", reply_markup=emoji_choice_keyboard)
    await update_emoji_profile_player.Q1.set()


@dp.message_handler(state=update_emoji_profile_player.Q1)
async def update_player_emoji_2(message: types.Message, state: FSMContext):
    add_last_message(message.chat.id)
    if emoji.emoji_count(message.text) >= 1:
        if emoji.emoji_count(message.text) == 1:
            if message.text in "🟥🟧🟨🟩🟦🟪⬜🟫⬛🔴🟠🟡🟢🔵🟣⚪🟤⚫":
                await message.answer(f"✅ Эмодзи принят.", reply_markup=main_keyboard)
                update_emoji_player(message.chat.id, message.text)
                await state.finish()
                await my_profile(message)
            else:
                await message.answer("⤵ Выбери эмодзи на клавиатуре снизу.")
        elif emoji.emoji_count(message.text) >= 2:
            await message.answer("1️⃣ Введите только одно эмодзи!")
    else:
        await message.answer("🫥 Вы ввели не эмодзи!")