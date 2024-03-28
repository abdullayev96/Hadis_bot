from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

tasdiqlash = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tasdiqlash", callback_data="tasdiqlash"),
            InlineKeyboardButton(text="Taxrirlash", callback_data="taxrirlash")
        ]
    ]
)