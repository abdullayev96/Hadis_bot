from keyboards.default.admin import admin, adminbutton, bekor
import asyncio
from loader import dp, db, bot
from aiogram.types import InputFile
from aiogram.dispatcher import FSMContext
from aiogram import types





@dp.message_handler(commands='admin', state='*', chat_id=614916220)
async def edfgt(message:types.Message, state:FSMContext):
 await state.finish()
 await message.answer("🔝 Asosiy menyu", reply_markup=admin)




@dp.message_handler(text='📥Bazani yuklab olish', chat_id=614916220)
async def dowloadfile(message:types.Message):
    file = InputFile(path_or_bytesio='data/main.db')
    await message.answer_document(file)




@dp.message_handler(text="📊Obunachilar soni", chat_id=614916220)
async def son(message:types.Message):
    jami = db.count_users()[0]
    son = db.count_users()
    await message.answer(f"Foydalanuvchilar soni: {jami} ta\nHadislar soni: {son} ta")



@dp.message_handler(text="✅Reklama yuborish", chat_id=614916220)
async def reklama(message:types.Message):
    await message.answer("Yuborish turini tanlang:", reply_markup=adminbutton)

@dp.message_handler(text="Tugmasiz", chat_id=614916220)
async def tugmasiz(message: types.Message, state: FSMContext):
    await message.answer("<b>📣 Reklama</b>\n\n"
                              "Reklama yuborishda bironta kanaldan reklamani forward (uzatish)ingiz mumkin\n"
                              "Ammo bot a'zolariga borgan reklama forward bo'lib emas. Oddiy reklama bo'lib boradi\n"
                              "Hamda reklamangizda inline tugmalar bo'lsa u ham yuborilmaydi\n\n"
                              "<i>Marhamat, reklamangizni yuboring</i>", reply_markup=bekor)
    await state.set_state('reklamatime')

@dp.message_handler(state='reklamatime', content_types=types.ContentTypes.ANY, chat_id=6383786874)
async def rek_text(message:types.Message, state: FSMContext):
    await state.finish()
    if message.text == "Bekor qilish ❌":
        await message.answer("Bekor qilindi!", reply_markup=admin)
    else:
        users = db.select_all_users()
        x = 0
        y = 0
        i = await message.answer("✅ Reklama yuborilyapti, iltimos kutib turing...")
        for user in users:
            try:
                await bot.copy_message(chat_id=user[0],
                                       from_chat_id=message.from_user.id,
                                       message_id=message.message_id)
                x += 1
            except:
                y += 1
            await asyncio.sleep(0.05)

        await i.delete()
        await message.answer("<b>✅ Reklama yuborildi</b>\n\n"
                             f"Qabul qildi: {x} ta\n"
                             f"Yuborilmadi: {y} ta")
        await message.answer("🔝 Asosiy menyu", reply_markup=admin)




@dp.message_handler(text="Tugmali", chat_id=614916220)
async def tugmasiz(message: types.Message, state: FSMContext):
    await message.answer("Tugma nomi va urlni kiriting:\n\nNamuna: Kanalnomi+url,Botnomi+url")
    await state.set_state('tugmali')

@dp.message_handler(state ="tugmali", chat_id=614916220)
async def tugmasiz(message: types.Message, state: FSMContext):
    await state.update_data(tugma111=message.text)
    await message.answer("Reklama postini yuboring!")
    await state.set_state("rekpost")

@dp.message_handler(state ="rekpost", content_types=types.ContentType.ANY, chat_id=614916220)
async def tugmasiz(message: types.Message, state: FSMContext):
    data = await state.get_data()
    button_name = str(data.get("tugma111")).split(',')
    button = types.InlineKeyboardMarkup(row_width=1)
    for b in button_name:
        tugma = b.split('+')
        button.insert(types.InlineKeyboardButton(text=tugma[0], url=tugma[1]))
    x =  await message.copy_to(chat_id=message.from_user.id, reply_markup=button)
    await message.answer(f"Reklama id: <code>{x.message_id}</code>", reply_markup=bekor)
    await state.set_state('yubor')

@dp.message_handler(state ="yubor", chat_id=614916220)
async def yuborish(message: types.Message, state: FSMContext):
    if message.text == "Bekor qilish ❌":
        await message.answer("Bekor qilindi!", reply_markup=admin)
    else:
        data = await state.get_data()
        button_name = str(data.get("tugma111")).split(',')
        button = types.InlineKeyboardMarkup(row_width=1)
        for b in button_name:
            tugma = b.split('+')
            button.insert(types.InlineKeyboardButton(text=tugma[0], url=tugma[1]))
        users = db.select_all_users()
        x = 0
        y = 0
        i = await message.answer("✅ Reklama yuborilyapti, iltimos kutib turing...")
        for user in users:
            try:
                await bot.copy_message(chat_id=user[0],
                                       from_chat_id=message.from_user.id,
                                       message_id=int(message.text), reply_markup=button)
                x += 1
            except:
                y += 1
            await asyncio.sleep(0.05)

        await i.delete()
        await message.answer("<b>✅ Reklama yuborildi</b>\n\n"
                             f"Qabul qildi: {x} ta\n"
                             f"Yuborilmadi: {y} ta")
        await state.finish()
        await message.answer("🔝 Asosiy menyu", reply_markup=admin)

