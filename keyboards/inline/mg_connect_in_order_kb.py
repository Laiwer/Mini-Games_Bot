from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


start_connect_in_order_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="back_connect_in_order"),
            InlineKeyboardButton(text="▶️ Начать", callback_data="start_connect_in_order")
        ]
    ]
)

end_connect_in_order_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Закончить", callback_data="end_connect_in_order")
        ]
    ]
)