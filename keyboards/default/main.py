from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🧩 Мини-игры"),
        ],
        [
            KeyboardButton(text="🏆 Рейтинг"),
            KeyboardButton(text="📊 Статистика"),
        ],
        [
            KeyboardButton(text="👤 Профиль"),
            KeyboardButton(text="👥 Рефералы"),
        ]
    ],
    resize_keyboard=True
)