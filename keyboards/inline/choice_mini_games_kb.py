from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


mini_games_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔎 Найди эмодзи", callback_data="Найди эмодзи")
        ],
        [
            InlineKeyboardButton(text="🔢 Соединить по порядку", callback_data="Соединить по порядку")
        ],
        [
            InlineKeyboardButton(text="🎨 Одинаковые по цвету", callback_data="Одинаковые по цвету")
        ],
        [
            InlineKeyboardButton(text="🛒 Найти по списку", callback_data="Найти по списку")
        ],
        [
            InlineKeyboardButton(text="🔗 Собрать пару", callback_data="Собрать пару")
        ]
    ]
)
