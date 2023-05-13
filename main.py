import aiogram
TOKEN=open("token.txt", "r")
TOKEN = TOKEN.readline()
bot = aiogram.Bot(token=TOKEN)
dispatcher = aiogram.Dispatcher(bot)

@dispatcher.message_handler(commands=["start"])
async def start(message: aiogram.types.Message):
    await message.answer("Привет! Я твой чат бот и помощник разобраться с собой. Работаю в подходе IDEAL. Напиши в поле ниже с какими мыслями ты пришел ко мне и что хотел бы получить в результате?")


aiogram.executor.start_polling(dispatcher)