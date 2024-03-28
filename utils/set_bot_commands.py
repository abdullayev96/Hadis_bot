from aiogram import types
import asyncio
from loader import db


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("language", "Tilni o'zgartirish")
        ]
    )

