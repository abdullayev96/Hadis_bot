from aiogram import types
from loader import dp, db
from aiogram.dispatcher import FSMContext
from keyboards.inline.bosh_menu import bosh_menu_uz, bosh_menu_ru
from keyboards.inline.bosh_menu_qaytish import ortga_qaytish_uz, ortga_qaytish_ru



@dp.callback_query_handler(text=["boshmenyu", "uz", "ru"], state="*")
async def tasdiqlash1(call: types.CallbackQuery, state:FSMContext):

    if call.data == "boshmenyu":
        user = db.select_user(call.from_user.id)
        if user[3] == "uz":
            await call.message.edit_text("Asosiy menyuga xush kelibsiz!", reply_markup=bosh_menu_uz)
            await state.finish()
        elif user[3] == "ru":
            await call.message.edit_text("Добро пожаловать в главное меню", reply_markup=bosh_menu_ru)
            await state.finish()


    else:
        if call.data == "uz":
            db.update_language(language="uz", id=call.from_user.id)
            await call.message.edit_text("Asosiy menyuga xush kelibsiz!", reply_markup=bosh_menu_uz)
            await state.finish()

        elif call.data == "ru":
            db.update_language(language="ru", id=call.from_user.id)
            await call.message.edit_text("Добро пожаловать в главное меню", reply_markup=bosh_menu_ru)
            await state.finish()




@dp.callback_query_handler(text="top")
async def tasdiqlash1(call: types.CallbackQuery):
    user = db.select_user(call.from_user.id)
    day = db.top_day()
    week= db.top_week()
    forever = db.top_forever()
    result1 = str()
    result2 = str()
    result3 = str()
    raqam1 = 1
    raqam2 = 1
    raqam3 = 1
    for f in forever:
        if f[2]:
            result1 =  result1 + f"<b>{raqam1} .</b> <a href='https://t.me/{f[2]}'>{f[1]}</a>  <b>{f[7]} </b> 📖\n"
            raqam1 = raqam1+1
        else:
            result1 = result1 + f"<b>{raqam1} .</b> {f[1]}  <b>{f[7]} </b> 📖\n"
            raqam1 = raqam1 + 1
    for w in week:
        if w[2]:
            result2 = result2 + f"<b>{raqam2} .</b> <a href='https://t.me/{w[2]}'>{w[1]}</a>  <b>{w[6]} </b> 📖\n"
            raqam2 = raqam2 + 1
        else:
            result2 = result2 + f"<b>{raqam2} .</b> {w[1]}  <b>{w[6]} </b> 📖\n"
            raqam2 = raqam2 + 1
    for d in day:
        if d[2]:
            result3 = result3 + f"<b>{raqam3} .</b> <a href='https://t.me/{d[2]}'>{d[1]}</a>  <b>{d[5]} </b> 📖\n"
            raqam3 = raqam3 + 1
        else:
            result3 = result3 + f"<b>{raqam3} .</b> {d[1]}  <b>{d[5]} </b> 📖\n"
            raqam3 = raqam3 + 1


    if user[3] == "uz":
        await call.message.edit_text(text=f"<b>🏆 Ummumiy top reyting:</b>\n{result1}\n\n<b>🏆 Hafta top reyting:</b>"
                                         f"\n{result2}\n\n🏆 <b>Kunlik top reyting:</b>\n{result3}",
                                    reply_markup=ortga_qaytish_uz, disable_web_page_preview=True)
    elif user[3] == "ru":
        await call.message.edit_text(text=f"<b>🏆 Общий высший рейтинг:</b>\n{result1}\n\n<b>🏆 Высший рейтинг за неделю:</b>"
                                          f"\n{result2}\n\n🏆 <b>Высший рейтинг за день:</b>\n{result3}",
                                     reply_markup=ortga_qaytish_ru, disable_web_page_preview=True)




@dp.callback_query_handler(text="mening")
async def tasdiqlash1(call: types.CallbackQuery):
    result = db.select_user(call.from_user.id)
    son = db.count_hadis()
    try:
        foiz = int((result[7] * 100) / son[0])
    except:
        foiz = 0
    if result[3] == "uz":
        await call.message.edit_text(
            f"📊 Sizning barcha statistikalaringiz:\n\n📖 Siz o'qigan hadislar soni: <b>{result[7]}</b> ta"
            f"\n🔋 Siz jami hadislarning <b>{foiz}%</b> o'qigansiz!\n"
            f"📆 Siz bir haftada <b>{result[6]}</b> ta hadis o'qiyapsiz!\n"
            f"📆 Siz bir kunda <b>{result[5]}</b> ta hadis o'qiyapsiz!\n"
            f"👥 Siz taklif qilgan odamlar soni: <b>{result[9]}</b> ta", reply_markup=ortga_qaytish_uz)



    else:
        await call.message.edit_text(
            f"📊 Вся ваша статистика:\n\n📖 Количество хадисов, которые вы прочитали: <b>{result[7]}</b> ta"
            f"\n🔋Вы прочитали <b>{foiz}%</b> от общего числа хадисов! \n"
            f"📆 Вы читаете <b>{result[6]}</b> хадис за неделю!\n"
            f"📆 Вы прочитали <b>{result[5]}</b> хадисов за один день!\n"
            f"👥 Количество приглашенных вами людей: <b>{result[9]}</b>", reply_markup=ortga_qaytish_ru)





@dp.callback_query_handler(text='friend')
async def friend(call: types.CallbackQuery, state:FSMContext):
    user = db.select_user(call.from_user.id)
    await state.set_state("friend_search")
    if user[3] == "uz":
        search_uz = types.InlineKeyboardMarkup(row_width=2)
        search_uz.add(types.InlineKeyboardButton(text="↩️ Bosh menyu!", callback_data="boshmenyu"),
                      types.InlineKeyboardButton(text="🔎 Do'stlarni qidirish!", switch_inline_query_current_chat=""))
        await call.message.edit_text("Qidirmoqchi bo'lgan do'stingiz kiriting:", reply_markup=search_uz)

    elif user[3] == "ru":
        search_ru = types.InlineKeyboardMarkup(row_width=2)
        search_ru.add(types.InlineKeyboardButton(text="↩️ Главное меню!", callback_data="boshmenyu"),
                      types.InlineKeyboardButton(text="🔎 Ищите друзей!", switch_inline_query_current_chat=""))
        await call.message.edit_text("Введите друга, которого хотите найти:", reply_markup=search_ru)






