from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
bosh_menu_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📖 Hadislar!", callback_data="hadislar"),
            InlineKeyboardButton(text="📚 Kerakli kitoblar!", callback_data="kitoblar")
        ],
        [
            InlineKeyboardButton(text="🔎 Do'stlarni qidirish!", callback_data="friend"),
            InlineKeyboardButton(text="🔎 Hadis qidirish!", switch_inline_query_current_chat="")

        ],
        [
            InlineKeyboardButton(text="🏆 Top reyting!", callback_data="top"),
            InlineKeyboardButton(text="📊 Mening statistikam!", callback_data="mening"),
        ],
        [
            InlineKeyboardButton(text="👥 Botni yaqinlarga ulashish!", switch_inline_query="ulashish")
        ]
    ]
)



bosh_menu_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📖 Хадисы", callback_data="hadislar"),
            InlineKeyboardButton(text="📚 Необходимые книги", callback_data="kitoblar")
        ],
        [
            InlineKeyboardButton(text="🔎 Поиск друзей", callback_data="friend"),
            InlineKeyboardButton(text="🔎 Поиск хадисов", switch_inline_query_current_chat="")

        ],
        [
            InlineKeyboardButton(text="🏆 Высший рейтинг", callback_data="top"),
            InlineKeyboardButton(text="📊 Моя статистика", callback_data="mening"),
        ],
        [
            InlineKeyboardButton(text="👥 Поделитесь ботом с близкими", switch_inline_query="ulashish")
        ]
    ]
)