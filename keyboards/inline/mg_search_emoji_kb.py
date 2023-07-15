from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


size_field_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="▫️ Легкий (3 x 3)", callback_data="3x3")
        ],
        [
            InlineKeyboardButton(text="◽ Средний (5 x 5)", callback_data="5x5")
        ],
        [
            InlineKeyboardButton(text="◻️ Сложный (7 x 7)", callback_data="7x7")
        ],
        [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="back:mini_games")
        ]
    ]
)

start_search_emoji_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="back_search_emoji_size"),
            InlineKeyboardButton(text="▶️ Начать", callback_data="Начать")
        ]
    ]
)

continue_search_emoji_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⏩ Продолжить", callback_data="Начать")
        ]
    ]
)