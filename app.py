from aiogram import executor, types
from loader import dp, db
import logging
import asyncio
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)
    try:
        db.create_table_users()
        db.create_table_week()
        db.create_table_hadislar()
        db.create_table_book()
    except:
        pass




if __name__ == '__main__':
    executor.start_polling(dp,allowed_updates=types.AllowedUpdates.all(), on_startup=on_startup )

