from aiogram import types
from loader import dp, db, bot




@dp.inline_handler(text="ulashish")
async def ulashish(query:types.InlineQuery):
    user = db.select_user(query.from_user.id)
    if user[3] == "uz":
        await query.answer(results=[
            types.InlineQueryResultArticle(
                id=f"56464dfg45654rt",
                title="Botni ulashish uchun ustiga bosing!",
                input_message_content=types.InputTextMessageContent(message_text=f"https://t.me/BOT?start={query.from_user.id}"),
                description="Nimadir"
            )
        ], cache_time=1000)

    elif user[3] == "ru":
        bot_info = await bot.get_me()
        await query.answer(results=[
            types.InlineQueryResultArticle(
                id=f"56464dfg45654rt",
                title="Нажмите, чтобы поделиться ботом!",
                input_message_content=types.InputTextMessageContent(
                    message_text=f"https://t.me/{bot_info.username}?start={query.from_user.id}"),

            )
        ], cache_time=1000)



@dp.inline_handler(state="friend_search")
async def inline_qidiruv(query: types.InlineQuery):
    user1 = db.select_user(query.from_user.id)
    son = db.count_hadis()
    if query.query:
        all_users = db.search_user(name=query.query)
        all_result = []
        for user in all_users:
            try:
                foiz = int((user[7] * 100) / son[0])
            except:
                foiz = 0
            if user1[3] == "uz":
                all_result.append(
                    types.InlineQueryResultArticle(
                        id=f"id{user[0]}",
                        title=f"{user[1]}",
                        input_message_content=types.InputTextMessageContent(
                            message_text=f"📖 {user[1]} o'qigan hadislar soni: <b>{user[7]}</b> ta\n"
                                         f"👥 {user[1]} taklif qilgan odamlar soni: <b>{user[9]}</b> ta\n"
                                         f"📅 {user[1]} bir haftada <b>{user[6]}</b> ta hadis o'qiyapti!\n"
                                         f"📆 {user[1]} bir kunda <b>{user[5]}</b> ta hadis o'qiyapti\n"
                                         f"🔋 {user[1]} jami hadislarning <b>{foiz}%</b> o'qigansiz!\n"),
                        description=f"Fodalanuvchi haqida qisqacha ma'lumot",
                        thumb_url="https://i.pinimg.com/736x/2d/75/50/2d7550d033be4f1f61b27bce357f6ff0.jpg",
                    )
                )
            elif user1[3] == "ru":
                all_result.append(
                    types.InlineQueryResultArticle(
                        id=f"id{user[0]}",
                        title=f"{user[1]}",
                        input_message_content=types.InputTextMessageContent(
                            message_text=f"📖 Количество хадисов, прочитанных пользователем {user[1]}: <b>{user[7]}</b>\n"
                                         f"👥 Количество людей, приглашенных пользователем {user[1]}: <b>{user[9]}</b>\n"
                                         f"📅 {user[1]} читает <b>{user[6]}</b> хадис за неделю!\n"
                                         f"📆 {user[1]} читает <b>{user[5]}</b> хадис за один день\n"
                                         f"🔋 Пользователь {user[1]} прочитал <b>{foiz}%</b> от общего числа хадисов!\n"),
                        description=f"Fodalanuvchi haqida qisqacha ma'lumot",
                        thumb_url="https://i.pinimg.com/736x/2d/75/50/2d7550d033be4f1f61b27bce357f6ff0.jpg",
                    )
                )

        await query.answer(all_result, cache_time=1)
    else:
        all_users = db.search_user_random()
        all_result = []
        for user in all_users:
            try:
                foiz = int((user[7] * 100) / son[0])
            except:
                foiz = 0
            if user[3] == "uz":
                all_result.append(
                    types.InlineQueryResultArticle(
                        id=f"id{user[0]}",
                        title=f"{user[1]}",
                        input_message_content=types.InputTextMessageContent(
                            message_text=f"📖 {user[1]} o'qigan hadislar soni: <b>{user[7]}</b> ta\n"
                                         f"👥 {user[1]} taklif qilgan odamlar soni: <b>{user[9]}</b> ta\n"
                                         f"📅 {user[1]} bir haftada <b>{user[6]}</b> ta hadis o'qiyapti!\n"
                                         f"📆 {user[1]} bir kunda <b>{user[5]}</b> ta hadis o'qiyapti\n"
                                         f"🔋 {user[1]} jami hadislarning <b>{foiz}%</b> o'qigansiz!\n"),
                        description=f"Fodalanuvchi haqida qisqacha ma'lumot",
                        thumb_url="https://i.pinimg.com/736x/2d/75/50/2d7550d033be4f1f61b27bce357f6ff0.jpg",
                    )
                )
            elif user1[3] == "ru":
                all_result.append(
                    types.InlineQueryResultArticle(
                        id=f"id{user[0]}",
                        title=f"{user[1]}",
                        input_message_content=types.InputTextMessageContent(
                            message_text=f"📖 Количество хадисов, прочитанных пользователем {user[1]}: <b>{user[7]}</b> ta\n"
                                         f"👥 Количество людей, приглашенных пользователем {user[1]}: <b>{user[9]}</b> ta\n"
                                         f"📅 {user[1]} читает <b>{user[6]}</b> хадис за неделю!\n"
                                         f"📆 {user[1]} читает <b>{user[5]}</b> хадис за один день\n"
                                         f"🔋 Пользователь {user[1]} прочитал <b>{foiz}%</b> от общего числа хадисов!\n"),
                        description=f"Fodalanuvchi haqida qisqacha ma'lumot",
                        thumb_url="https://i.pinimg.com/736x/2d/75/50/2d7550d033be4f1f61b27bce357f6ff0.jpg",
                    )
                )

        await query.answer(all_result, cache_time=1)







@dp.inline_handler()
async def inline_qidiruv(query: types.InlineQuery):
    user = db.select_user(query.from_user.id)
    all_result = []
    if query.query:
        if user[3] == "uz":
            all_hadis = db.search_hadis_uz(query.query)
            for hadis in all_hadis:
                all_result.append(
                    types.InlineQueryResultArticle(
                        id=f"id{hadis[0]}",
                        title=f"{hadis[2]}",
                        input_message_content=types.InputTextMessageContent(message_text=f"{hadis[1]}"),
                        description=f"{hadis[1]}",
                        thumb_url="https://i.pinimg.com/736x/2d/75/50/2d7550d033be4f1f61b27bce357f6ff0.jpg",
                    )
                )

        elif user[3] == "ru":
            all_hadis = db.search_hadis_ar(query.query)
            for hadis in all_hadis:
                all_result.append(
                    types.InlineQueryResultArticle(
                        id=f"id{hadis[0]}",
                        title=f"{hadis[4]}",
                        input_message_content=types.InputTextMessageContent(message_text=f"{hadis[3]}"),
                        description=f"{hadis[3]}",
                        thumb_url="https://i.pinimg.com/736x/2d/75/50/2d7550d033be4f1f61b27bce357f6ff0.jpg",
                    )
                )


    else:
        if user[3] == "uz":
            all_hadis = db.search_hadis_random_uz()
            for hadis in all_hadis:
                all_result.append(
                    types.InlineQueryResultArticle(
                        id=f"id{hadis[0]}",
                        title=f"{hadis[2]}",
                        input_message_content=types.InputTextMessageContent(message_text=f"{hadis[1]}"),
                        description=f"{hadis[1]}",
                        thumb_url="https://i.pinimg.com/736x/2d/75/50/2d7550d033be4f1f61b27bce357f6ff0.jpg",
                    )
                )

        elif user[3] == "ru":
            all_hadis = db.search_hadis_random_ar()
            for hadis in all_hadis:
                all_result.append(
                    types.InlineQueryResultArticle(
                        id=f"id{hadis[0]}",
                        title=f"{hadis[4]}",
                        input_message_content=types.InputTextMessageContent(message_text=f"{hadis[3]}"),
                        description=f"{hadis[3]}",
                        thumb_url="https://i.pinimg.com/736x/2d/75/50/2d7550d033be4f1f61b27bce357f6ff0.jpg",
                    )
                )
