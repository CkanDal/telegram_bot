import requests
import os
import aiogram
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command, CommandStart
import asyncio
from dotenv import load_dotenv
import sys
sys.path.append("..")

from ips import get_ips
from traffic import get_speed

button_1 = KeyboardButton(text='/ips')
button_2 = KeyboardButton(text='/traffic')
button_3 = KeyboardButton(text='/speed')


keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2 ,button_3]], resize_keyboard=True)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
chat_id = os.getenv("chat_id")

bot = aiogram.Bot(BOT_TOKEN)
dp = aiogram.Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(text='Which commands I do execute ?', reply_markup=keyboard)

@dp.message(Command(commands='speed'))
async def gets_speed(message: Message):
   await message.answer(get_speed())

@dp.message(Command(commands='traffic'))
async def send_traffic(message: Message):
    with open("../jsonOutput.txt", "r", encoding="utf-8") as users:
        await message.answer(users.read())

@dp.message(Command(commands='ips'))
async def send_ip(message: Message):
    await message.answer(get_ips())

async def send_ips_cycle():
    while True:
        await bot.send_message(chat_id, get_ips())
        await asyncio.sleep(21600)
    


async def main():
    asyncio.create_task(send_ips_cycle())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
