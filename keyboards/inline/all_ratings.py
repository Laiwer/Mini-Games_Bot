from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


button_back_ratings = InlineKeyboardButton(text="⬅️ Назад", callback_data="back:ratings")
button_back_mini_games = InlineKeyboardButton(text="⬅️ Назад", callback_data="back:ratings_mini_games")
button_back_mini_games_size = InlineKeyboardButton(text="⬅️ Назад", callback_data="ratings_mini_games_size")

all_ratings_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🏆 Всего трофеев", callback_data="Всего трофеев")
        ],
        [
            InlineKeyboardButton(text="🎮 Мини-игры", callback_data="rating_mini_games")
        ],
        [
            InlineKeyboardButton(text="👥 Количество рефералов", callback_data="Количество рефералов")
        ],
    ]
)

mini_games_rating_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔎 Найди эмодзи", callback_data="record_search_emoji")
        ],
        [
            InlineKeyboardButton(text="🔢 Соединить по порядку", callback_data="record_connect_in_order")
        ],
        [
            button_back_ratings
        ]
    ]
)

mini_game_record_search_emoji_rating_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="3 x 3", callback_data="record_3x3")
        ],
        [
            InlineKeyboardButton(text="5 x 5", callback_data="record_5x5")
        ],
        [
            InlineKeyboardButton(text="7 x 7", callback_data="record_7x7")
        ],
        [
            button_back_mini_games
        ]
    ]
)

trophies_rating_keyboard_top = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🏅 Пятёрка лидеров", callback_data="ratings:top:trophies")
        ],
        [
            button_back_ratings
        ]
    ]
)

trophies_rating_keyboard_near = InlineKeyboardMarkup(
    inline_keyboard=[   
        [
            InlineKeyboardButton(text="👥 Игроки около вас", callback_data="ratings:you:trophies")
        ],
        [
            button_back_ratings
        ]
    ]
)


count_referal_rating_keyboard_top = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🏅 Пятёрка лидеров", callback_data="ratings:top:count_referal")
        ],
        [
            button_back_ratings
        ]
    ]
)

count_referal_rating_keyboard_near = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👥 Игроки около вас", callback_data="ratings:you:count_referal")
        ],
        [
            button_back_ratings
        ]
    ]
)


record_search_emoji_small_rating_keyboard_top = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🏅 Пятёрка лидеров", callback_data="ratings:top:r_search_e_small")
        ],
        [
            button_back_mini_games_size
        ]
    ]
)

record_search_emoji_small_rating_keyboard_near = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👥 Игроки около вас", callback_data="ratings:you:r_search_e_small")
        ],
        [
            button_back_mini_games_size
        ]
    ]
)


record_search_emoji_medium_rating_keyboard_top = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🏅 Пятёрка лидеров", callback_data="ratings:top:r_search_e_medium")
        ],
        [
            button_back_mini_games_size
        ]
    ]
)

record_search_emoji_medium_rating_keyboard_near = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👥 Игроки около вас", callback_data="ratings:you:r_search_e_medium")
        ],
        [
            button_back_mini_games_size
        ]
    ]
)


record_search_emoji_hard_rating_keyboard_top = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🏅 Пятёрка лидеров", callback_data="ratings:top:r_search_e_hard")
        ],
        [
            button_back_mini_games_size
        ]
    ]
)

record_search_emoji_hard_rating_keyboard_near = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👥 Игроки около вас", callback_data="ratings:you:r_search_e_hard")
        ],
        [
            button_back_mini_games_size
        ]
    ]
)


record_connect_in_order_keyboard_top = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🏅 Пятёрка лидеров", callback_data="ratings:top:connect_in_order")
        ],
        [
            button_back_mini_games
        ]
    ]
)

record_connect_in_order_keyboard_near = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👥 Игроки около вас", callback_data="ratings:you:connect_in_order")
        ],
        [
            button_back_mini_games
        ]
    ]
)