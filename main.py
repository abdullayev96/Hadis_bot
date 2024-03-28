from fastapi import FastAPI
from loader import dp, bot
from utils.notify_admins import on_startup_notify
from aiogram import Dispatcher, Bot
from aiogram import types
from data.config import BOT_TOKEN

app = FastAPI()

WEBHOOK_PATH = f"/{BOT_TOKEN}/"
WEBHOOK_URL = "https://c534-188-113-198-104.ngrok.io"+WEBHOOK_PATH

@app.on_event("startup")
async def on_startup():
    url = await bot.get_webhook_info()
    if url != WEBHOOK_URL:
        await bot.set_webhook(url=WEBHOOK_URL)
        await on_startup_notify(dp)


@app.post(WEBHOOK_PATH)
async def botwebhook(update:dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.get_session().close()


