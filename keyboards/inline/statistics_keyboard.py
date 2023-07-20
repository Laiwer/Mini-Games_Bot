from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


all_statistics_keyboards = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🕹 Статистика мини-игр", callback_data="Статистика мини-игр")
        ]
    ]
)


mini_games_statistics_keyboards = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔎 Найди эмодзи", callback_data="stata_search_emoji")
        ],
        [
            InlineKeyboardButton(text="🔢 Соединить по порядку", callback_data="stata_connect_in_order")
        ],
        [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_statistics")
        ]
    ]
)


back_from_mini_game_statistics_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_mini_game_statistics")
        ]
    ]
)