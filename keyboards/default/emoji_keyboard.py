from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


emoji_choice_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🟥"),
            KeyboardButton(text="🔴"),
            KeyboardButton(text="🟩"),
            KeyboardButton(text="🟢"),
            KeyboardButton(text="⬜"),
            KeyboardButton(text="⚪"),
        ],
        [
            KeyboardButton(text="🟧"),
            KeyboardButton(text="🟠"),
            KeyboardButton(text="🟦"),
            KeyboardButton(text="🔵"),
            KeyboardButton(text="🟫"),
            KeyboardButton(text="🟤"),
        ],
        [
            KeyboardButton(text="🟨"),
            KeyboardButton(text="🟡"),
            KeyboardButton(text="🟪"),
            KeyboardButton(text="🟣"),
            KeyboardButton(text="⬛"),
            KeyboardButton(text="⚫"),
        ]
    ],
    resize_keyboard=True
)