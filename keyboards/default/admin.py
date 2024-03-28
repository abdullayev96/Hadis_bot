from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅Reklama yuborish"),
            KeyboardButton(text='📊Obunachilar soni'),

        ],
        [
            KeyboardButton(text="📥Bazani yuklab olish"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

adminbutton = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tugmali "),
            KeyboardButton(text="Tugmasiz "),

        ]

    ], resize_keyboard=True, one_time_keyboard=True
)

bekor = ReplyKeyboardMarkup(
    keyboard=[
          [
              KeyboardButton(text='Bekor qilish ❌')
          ]
    ],resize_keyboard=True, one_time_keyboard=True
)
