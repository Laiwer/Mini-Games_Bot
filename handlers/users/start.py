from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from dataBase.base import existe_in_db, add_user_in_data_base, existe_name_player, add_player_in_data_base, \
    update_emoji_player, add_last_message, add_mini_game_search_emoji_on_field_in_data_base, \
    existe_referrer_id, get_data_from_user, get_data_from_player
from keyboards.default.main import main_keyboard
from keyboards.default.emoji_keyboard import emoji_choice_keyboard
from states.create_player import create_player
from aiogram.dispatcher.storage import FSMContext
import string
from loader import dp, bot
import emoji


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if message.chat.type == "private":
        referrer_id = str(message.text[7:])
        if referrer_id != "":
            if referrer_id != str(message.from_user.id) and not existe_in_db("user", message.from_user.id):
                add_user_in_data_base(message.from_user.id, str(message.chat.username), message.chat.full_name, referrer_id)
            elif referrer_id == str(message.from_user.id):
                if not existe_in_db("user", message.from_user.id):
                    add_user_in_data_base(message.from_user.id, str(message.chat.username), message.chat.full_name)
                await message.answer("😡 Ты не можешь регистрироватся по своей реферальной ссылке!")
            elif not existe_in_db("user", int(referrer_id)):
                if not existe_in_db("user", message.from_user.id):
                    add_user_in_data_base(message.from_user.id, str(message.chat.username), message.chat.full_name)
                await message.answer("🤨 Откуда ты взял эту ссылку? Игрок с таким id не играет в бота, а значит реферальная ссылка не действительна!")
            else:
                await message.answer("🤷 Ты уже начал играть и не можешь быть рефералом!")
        else:
            if not existe_in_db("user", message.from_user.id):
                add_user_in_data_base(message.from_user.id, str(message.chat.username), message.chat.full_name)

        if not existe_in_db("player", message.from_user.id):
            await message.answer("🤔 Придумай никнейм и напиши его ниже.")
            await message.answer("🔡 В никнейме могут быть только: буквы латиницы (a-z, A-Z), цифры (0-9) и подчёркивание (_).")
            await message.answer("↔ Максимальная длина никнейма - 15 символов.")
            await message.answer("❗ В будущем никнейм поменять будет <b><u>нельзя</u></b>!")
            await create_player.Q1.set()
        else:
            await message.answer(f"🎮 <b>Давай начнём играть!</b>", reply_markup=main_keyboard)


@dp.message_handler(state=create_player.Q1)
async def create_buisness_1(message: types.Message):
    if message.chat.type == "private":
        add_last_message(message.from_user.id)
        LETNUM = f"{string.ascii_letters}{string.digits}_"
        if len(message.text) <= 15:
            if not existe_name_player(message.text):
                player_name = False
                for i in message.text:
                    if i in LETNUM:
                        player_name = True
                    else:
                        await message.answer("🛑 Введи символы которые разрешены!")
                        player_name = False
                        break
                if player_name:
                    await message.answer(f"✅ Никнейм принят.")
                    add_player_in_data_base(message.from_user.id, message.text, "⬜️")
                    await message.answer("😀 Теперь выберите эмодзи, который будет перед вашим ником.", reply_markup=emoji_choice_keyboard)
                    await message.answer("▶️ Как будет выглядеть: ⬜️player")
                    await create_player.Q2.set()
            else:
                await message.answer("ℹ️ Игрок с таким именем уже существует!")
        else:
            await message.answer("↔ Длина ника не больше 15 символов!")



@dp.message_handler(state=create_player.Q2)
async def create_buisness_2(message: types.Message, state: FSMContext):
    if message.chat.type == "private":
        add_last_message(message.from_user.id)
        if emoji.emoji_count(message.text) >= 1:
            if emoji.emoji_count(message.text) == 1:
                if message.text in "🟥🟧🟨🟩🟦🟪⬜🟫⬛🔴🟠🟡🟢🔵🟣⚪🟤⚫":
                    await message.answer(f"✅ Эмодзи принят.")
                    update_emoji_player(message.from_user.id, message.text)
                    add_mini_game_search_emoji_on_field_in_data_base(message.from_user.id)
                    await message.answer("🎮 <b>Давай начнём играть!</b>", reply_markup=main_keyboard)

                    if existe_referrer_id(get_data_from_user(message.from_user.id)[4]):
                        try:
                            refer = get_data_from_user(message.from_user.id)[4]
                            name_refer = get_data_from_player(message.from_user.id)
                            name_main = get_data_from_player(refer)
                            await bot.send_message(refer, f"✨ По вашей реферальной ссылке был зарегистрирован игрок:\n{name_refer[1]} <b>{name_refer[0]}</b>")
                            await message.answer(f"✨ Вы были зарегистрированы через реферальную ссылку игрока:\n{name_main[1]} <b>{name_main[0]}</b>")
                        except Exception: pass
                    
                    await state.finish()
                else:
                    await message.answer("⤵ Выбери эмодзи на клавиатуре снизу.")
            elif emoji.emoji_count(message.text) >= 2:
                await message.answer("1️⃣ Введите только одно эмодзи.")
        else:
            await message.answer("🫥 Вы ввели не эмодзи.")