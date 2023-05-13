import aiogram
TOKEN=open("token.txt", "r")
TOKEN = TOKEN.readline()
bot = aiogram.Bot(token=TOKEN)
dispatcher = aiogram.Dispatcher(bot)

@dispatcher.message_handler(commands=["start"])
async def start(message: aiogram.types.Message):
    await message.answer("Привіт!")
    keyboard = aiogram.types.InlineKeyboardMarkup()
    #Сюди треба додавати кнопки
    keyboard.add(aiogram.types.InlineKeyboardButton("Перша кнопка", callback_data="first"))
    keyboard.add(aiogram.types.InlineKeyboardButton("Друга кнопка", callback_data="second"))
    await message.answer("Тестові кнопки", reply_markup=keyboard)

@dispatcher.callback_query_handler()
async def callback(query: aiogram.types.CallbackQuery):
    #Перевірка на натискання кнопки
    if query.data == "first":
        await bot.send_message(query.from_user.id, "Перша кнопка")
    elif query.data == "second":
        await bot.send_message(query.from_user.id, "Друга кнопка")

aiogram.executor.start_polling(dispatcher)