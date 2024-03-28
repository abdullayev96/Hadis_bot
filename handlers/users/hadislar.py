import asyncio
from aiogram.dispatcher.filters import Text
from aiogram import types
from for_time import result_time ,return_tosh
from loader import dp, db, bot
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text="hadislar")
async def xadislar(call:types.CallbackQuery):
    user = db.select_user(id=call.from_user.id)
    text = db.random_hadis()
    if user[3] == "uz":
        hadis_button = types.InlineKeyboardMarkup(row_width=2)
        hadis_button.add(types.InlineKeyboardButton(text="◀️ Ortga", callback_data="hadislar"),
                         types.InlineKeyboardButton(text="Oldinga ▶️", callback_data="hadislar"),
                         types.InlineKeyboardButton(text="✅ O'qidim!", callback_data=f"read.{text[0]}"),
                         types.InlineKeyboardButton(text="📬 Botni ulashish!!", switch_inline_query="ulashish"),
                         types.InlineKeyboardButton(text="↩️ Bosh menyu!", callback_data="boshmenyu"))
        try:
            await call.message.edit_text(text=f"{text[1]}", reply_markup=hadis_button)
        except:
            text = db.random_hadis()
            await call.message.edit_text(text=f"{text[1]}", reply_markup=hadis_button)

    elif user[3] == "ru":
        hadis_button = types.InlineKeyboardMarkup(row_width=2)
        hadis_button.add(types.InlineKeyboardButton(text="◀️ Назад", callback_data="hadislar"),
                         types.InlineKeyboardButton(text="Вперед ▶️", callback_data="hadislar"),
                         types.InlineKeyboardButton(text="✅ Я читаю!", callback_data=f"read.{text[0]}"),
                         types.InlineKeyboardButton(text="📬 Поделитесь ботом!", switch_inline_query="ulashish"),
                         types.InlineKeyboardButton(text="↩️ Главное меню!", callback_data="boshmenyu"))
        try:
            await call.message.edit_text(text=f"{text[3]}", reply_markup=hadis_button)
        except:
            text = db.random_hadis()
            await call.message.edit_text(text=f"{text[3]}", reply_markup=hadis_button)






@dp.callback_query_handler(Text(startswith="read."))
async def read(call: types.CallbackQuery):
    hadis_id = call.data.split(".")[1]
    user = db.select_user(id=call.from_user.id)
    last_time = str(user[4])
    time = result_time(call_time=str(return_tosh()), last_time=last_time)
    if time < 20:
        if user[3] == "uz":
            await call.answer("Kechirasiz siz bu funksiyadan vaqtincha foydalana olmaysiz!", show_alert=True)
        elif user[3] == "ru":
            await call.answer("Извините, эта функция временно недоступна!", show_alert=True)
        await asyncio.sleep(1)
    else:
        r = db.return_four(call.from_user.id)
        all_read = str(r[3]).split(".")
        for one in all_read:
            if one == hadis_id:
                if user[3] == "uz":
                    await call.answer("Kechirasiz siz bu hadisni o'qigansiz", show_alert=True)
                elif user[3] == "ru":
                    await call.answer("Извините, вы прочитали этот хадис", show_alert=True)
                return
        if user[3] == "uz":
            await call.answer("O'qildi!", show_alert=True)
        elif user[3] == "ru":
            await call.answer("Прочтите это!", show_alert=True)
        db.time_update(new_time=return_tosh(), id=call.from_user.id)
        d = 1+r[0]
        w = 1+r[1]
        f = 1+r[2]
        read = f"{r[3]}"+f".{hadis_id}"
        db.update_four(day=d,week=w,forever=f, read=read, id=call.from_user.id)




@dp.message_handler(commands="hadis")
async def hadisplus(message: types.Message, state:FSMContext):
    await message.answer("Hadisni kiriting: (UZBEKCHA)")
    await state.set_state("hadis_uz")


@dp.message_handler(state="hadis_uz")
async def hadisplus(message: types.Message, state:FSMContext):
    await state.update_data(hadis_uz=message.text)
    await message.answer("Hadis sarlavhasini kiriting: (UZBEKCHA)")
    await state.set_state("hadis_uzs")

@dp.message_handler(state="hadis_uzs")
async def hadisplus(message: types.Message, state:FSMContext):
    await state.update_data(hadis_uzs=message.text)
    await message.answer("Hadisni kiriting: (RUSCHA)")
    await state.set_state("hadis_ru")




@dp.message_handler(state="hadis_ru")
async def hadisplus(message: types.Message, state:FSMContext):
    await state.update_data(hadis_ru=message.text)
    await message.answer("Hadisni sarlavhasini kiriting: (RUSCHA)")
    await state.set_state("hadis_rus")


@dp.message_handler(state="hadis_rus")
async def hadisplus(message: types.Message, state: FSMContext):
    await state.update_data(hadis_rus=message.text)
    data = await state.get_data()
    UZ = data.get("hadis_uz")
    UZ_S = data.get("hadis_uzs")
    RU = data.get("hadis_ru")
    RU_S = message.text
    db.add_hadis_3(UZ=UZ, UZ_S=UZ_S, RU=RU, RU_S=RU_S)
    await message.answer("Hadis joylandi!")
    await state.finish()


@dp.message_handler(commands="start_top", chat_id=614916220)
async def start_top(message: types.Message):
    await message.answer("Musobaqa boshlandi!")
    while True:
        await asyncio.sleep(6)
        db.update_day()
        day = db.return_day()
        if day:
            db.updata_day_w(update=day[0]+1)
        else:
            db.return_day_insert(update=1)
            continue
        if day[0] == 7:
            db.update_week()
            db.updata_day_w(update=0)

