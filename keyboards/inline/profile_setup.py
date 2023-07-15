from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


profile_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔄 Обновить профиль", callback_data="Обновить профиль")
        ],
        [
            InlineKeyboardButton(text="🔀 Поменять эмодзи", callback_data="Поменять эмодзи"),
        ]
    ]
)