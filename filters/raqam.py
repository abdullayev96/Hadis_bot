from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class Kod(BoundFilter):
    async def check(self,call: types.CallbackQuery):
        return call.data.isdigit()
