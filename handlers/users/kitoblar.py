from aiogram import types
from loader import db, dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from filters.raqam import Kod
from aiogram.dispatcher.filters import Text



@dp.message_handler(commands="kitob")
async def book(message:types.Message, state:FSMContext):
    await message.answer("Kerakli kitobni jo'nating:")
    await state.set_state("kitob")

@dp.message_handler(state="kitob", content_types=types.ContentType.DOCUMENT)
async def book_save(message:types.Message, state:FSMContext):
    book_name = message.document.file_name
    book_file_id = message.document.file_id
    db.book_save(book_name=book_name, book_id=book_file_id)
    await message.answer("Kitob joyland!")
    await state.finish()


@dp.callback_query_handler(text="kitoblar")
async def kitob(call: types.CallbackQuery, state:FSMContext):
    result = db.book_return()
    if len(result) <=10:
        miqdor = len(result)
        natija = InlineKeyboardMarkup(row_width=5)
        text = ''
        textson = 1
        for f in result[:10]:
            text += f"<b>{textson}.</b> {f[1]}\n"
            textson += 1
        son = 1
        for v in result[:10]:
            natija.insert(InlineKeyboardButton(text=f"{son}", callback_data=f"kitob.{v[0]}"))
            son += 1
        natija.row(InlineKeyboardButton(text="↩️", callback_data="boshmenyu"))
        await call.message.edit_text(f"<i>{text}</i>", reply_markup=natija)


    else:
        miqdor = len(result)
        natija = InlineKeyboardMarkup(row_width=5)
        text = ''
        textson = 1
        for f in result[:10]:
            text += f"<b>{textson}.</b> {f[1]}\n"
            textson += 1
        son = 1
        for v in result[:10]:
            natija.insert(InlineKeyboardButton(text=f"{son}", callback_data=f"kitob.{v[0]}"))
            son += 1
        natija.row(InlineKeyboardButton(text="↩️", callback_data="boshmenyu"),
                   InlineKeyboardButton(text='➡️', callback_data=1))
        await call.message.edit_text(f"<i>{text}</i>", reply_markup=natija)
        finally_result = []
        n = 10
        a = 0
        b = 10
        while miqdor + 10 > n:
            finally_result.append(result[a:b])
            a += 10
            b += 10
            n += 10
        await state.update_data(finally_result=finally_result)
        await state.update_data(topilgan_natijalar_soni=miqdor)


@dp.callback_query_handler(Kod())
async def plus_minus(call:types.CallbackQuery, state:FSMContext):
    data = await state.get_data()
    result = data.get('finally_result')
    topilgan_natijalar_soni = data.get('topilgan_natijalar_soni')
    try:
        miqdor = len(result) - 1
    except:
        await call.message.delete()
        return
    natija = InlineKeyboardMarkup(row_width=5)
    n = int(call.data)
    text = ''
    textson = 1
    try:
        for variable in result[0 + n]:
            text += f"<b>{textson}.</b> <i>{variable[1]}</i>\n"
            textson += 1
    except:
        await call.message.delete()
        return
    son = 1
    for v in result[0 + n]:
        natija.insert(InlineKeyboardButton(text=f"{son}", callback_data=v[0]))
        son += 1
    if  n == 0:
        t=10
        natija.row(InlineKeyboardButton(text="↩️", callback_data="boshmenyu"),InlineKeyboardButton(text='️➡️', callback_data=n + 1))

    elif n == miqdor:
        natija.row(InlineKeyboardButton(text='⬅️', callback_data=n - 1),InlineKeyboardButton(text="↪️", callback_data="boshmenyu"))
        t = topilgan_natijalar_soni

    else:
        natija.row(InlineKeyboardButton(text='⬅️', callback_data=n - 1),
                   InlineKeyboardButton(text='➡️', callback_data=n + 1))
        natija.row(InlineKeyboardButton(text="↩️", callback_data="boshmenyu"))
        t=(n+1)*10

    await call.message.edit_text(f'<i>{text}</i>')
    await call.message.edit_reply_markup(natija)


@dp.callback_query_handler(Text(startswith="kitob"))
async def book_send(call: types.CallbackQuery):
    id = call.data.split(".")[1]
    book_file_id = db.book_return_1(id=id)[0]
    await call.message.answer_document(document=book_file_id)



