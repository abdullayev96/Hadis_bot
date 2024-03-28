from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.private_chat import IsPrivate
from loader import dp, db, bot
from aiogram.dispatcher import FSMContext
from keyboards.inline.bosh_menu import bosh_menu_uz, bosh_menu_ru
from for_time import return_tosh


@dp.message_handler(IsPrivate(),CommandStart())
async def bot_start(message: types.Message, state:FSMContext):
    user = db.select_user(message.from_user.id)
    if message.get_args():
        if user:
            if user[3] == "uz":
                await message.answer("Asosiy menyuga xush kelibsiz!", reply_markup=bosh_menu_uz)

            elif user[3] == "ru":
                await message.answer("Добро пожаловать в главное меню", reply_markup=bosh_menu_ru)


        else:
            db.add_user(id=message.from_user.id, name=message.from_user.full_name,username=message.from_user.username, language="uz",time=return_tosh())
            button = types.InlineKeyboardMarkup(row_width=3)
            button.add(types.InlineKeyboardButton(text="🇺🇿 UZ", callback_data="uz"),
                       types.InlineKeyboardButton(text="🇷🇺 RU", callback_data="ru"))
            await message.answer(text="Iltimos tilni tanlang:\nПожалуйста, выберите язык:",
                                 reply_markup=button)
            old = db.friends_return(int(message.get_args()))
            new = old[0] + 1
            db.friends_update(friends=new, id=int(message.get_args()))
    else:
        if user:
            if user:
                if user[3] == "uz":
                    await message.answer("Asosiy menyuga xush kelibsiz!", reply_markup=bosh_menu_uz)

                else:
                    await message.answer("Добро пожаловать в главное меню", reply_markup=bosh_menu_ru)


        else:
            db.add_user(id=message.from_user.id, name=message.from_user.full_name, username=message.from_user.username, language="uz",time=return_tosh())
            button = types.InlineKeyboardMarkup(row_width=3)
            button.add(types.InlineKeyboardButton(text="🇺🇿 UZ", callback_data="uz"),
                       types.InlineKeyboardButton(text="🇷🇺 RU", callback_data="ru"))
            await message.answer(text="Iltimos tilni tanlang:\nПожалуйста, выберите язык:",
                                 reply_markup=button)
    await state.finish()



@dp.message_handler(commands="language", state="*")
async def change_language(message:types.Message):
    button = types.InlineKeyboardMarkup(row_width=3)
    button.add(types.InlineKeyboardButton(text="🇺🇿 UZ", callback_data="uz"),
               types.InlineKeyboardButton(text="🇷🇺 RU", callback_data="ru"))
    await message.answer(text="Iltimos tilni tanlang:\nПожалуйста, выберите язык:",
                         reply_markup=button)




@dp.chat_member_handler()
async def handle_chat_member(event: types.ChatMemberUpdated):
    if event.chat.id == -1001527619626:
        if event.new_chat_member.status == "member":
            # Send a welcome message to new members
            button = types.InlineKeyboardMarkup(row_width=3)
            button.add(types.InlineKeyboardButton(text="UZ", callback_data="uz"),
                       types.InlineKeyboardButton(text="RU", callback_data="ru"))
            await bot.send_message(text="Iltimos tilni tanlang:\nПожалуйста, выберите язык:",chat_id=event.new_chat_member.user.id,
            reply_markup=button)
        elif event.new_chat_member.status == "left":
            channel = await bot.get_chat(event.chat.id)
            button = types.InlineKeyboardMarkup(row_width=1)
            url = await channel.export_invite_link()
            button.insert(types.InlineKeyboardButton(text=f"{channel.title}", url=f"{url}"))
            await bot.send_message(chat_id=event.new_chat_member.user.id,
                                   text=f"Siz kanal a'zoligidan chiqib ketdingiz\n"
                                        f"Iltimos botdan foydalanish uchun kanalga a'zo bo'ling!\n\n"
                                        f"Вы отписались от канала\nПожалуйста, подпишитесь на канал, чтобы использовать бота", reply_markup=button)
    else:
        return


