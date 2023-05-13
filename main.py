import aiogram
import requests
import json


TOKEN=open("token.txt", "r")
TOKEN = TOKEN.readline()
bot = aiogram.Bot(token=TOKEN)
dispatcher = aiogram.Dispatcher(bot)

@dispatcher.message_handler(commands=["start"])
async def start(message: aiogram.types.Message):
    await message.answer("Привет! Я твой чат бот и помощник разобраться с собой. Работаю в подходе IDEAL. Напиши в поле ниже с какими мыслями ты пришел ко мне и что хотел бы получить в результате?")


@dispatcher.message_handler()
async def answer(message: aiogram.types.Message):
    str="Ты психолог который использует Тойча, чтобы решать все проблемы. К тебе пришел клиент и он говорит: "+message.text
    url = "https://tonai.tech/api/public/v1/services"
    payload ={
		'service_id': "6j99xutxsmiwpt6",
        'messages': str
    }
    headers={"key":"my_api_1_165b4b65-6b32-46d1-b794-0080fe26502c"}
    response = json.loads(requests.post(url, json=payload, headers=headers).text)
    print(response)

aiogram.executor.start_polling(dispatcher)