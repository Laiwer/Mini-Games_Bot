from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


mini_games_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔎 Найди эмодзи", callback_data="Найди эмодзи")
        ]
    ]
)
