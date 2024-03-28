from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import CHANNEL
from middlewares.check_sub import check_sub
from loader import bot


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
             user_id = update.message.from_user.id
        elif update.callback_query:
             user_id = update.callback_query.from_user.id
        else:
            return
        kanal = {}
        natija = True
        for channel in CHANNEL:
            result = await check_sub(user_id=user_id, channel=channel)
            natija = natija * result
            channel = await bot.get_chat(channel)

            if not result:
                link = await channel.export_invite_link()
                kanal[channel.title] = link

        tugma = InlineKeyboardMarkup(row_width=1)
        for key, variable in kanal.items():
            tugma.insert(InlineKeyboardButton(text="➕ Obuna bo'lish! ", url=f"{variable}"))
        if not natija:
            if update.message:
                await update.message.answer("Iltimos! Botdan foydalanish uchun kanalga obuna bo'lib qo'ying!\n"
                                            "Пожалуйста! Подпишитесь на канал, чтобы использовать бота!\n"
                                            "لو سمحت اشترك في القناة لاستخدام البوت", reply_markup=tugma)
                raise CancelHandler()
            elif update.callback_query:
                await update.callback_query.message.answer("Iltimos! Botdan foydalanish uchun kanalga obuna bo'lib qo'ying!\n"
                                                           "Пожалуйста! Подпишитесь на канал, чтобы использовать бота!\n"
                                                           "لو سمحت اشترك في القناة لاستخدام البوت", reply_markup=tugma)
                raise CancelHandler

