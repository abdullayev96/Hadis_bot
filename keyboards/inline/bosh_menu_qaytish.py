from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
ortga_qaytish_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Bosh menyu!", callback_data="boshmenyu"),
            InlineKeyboardButton(text="📬 Botni ulashish!", switch_inline_query="ulashish")
        ]
    ]
)



ortga_qaytish_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↩️ Главное меню", callback_data="boshmenyu"),
            InlineKeyboardButton(text="📬 Поделиться ботом", switch_inline_query="ulashish")
        ]
    ]
)