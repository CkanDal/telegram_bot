import requests
import os
import aiogram
from aiogram.types import Message
from aiogram.filters import Command
import asyncio
from dotenv import load_dotenv
import sys
sys.path.append("..")

from ips import get_ips
from traffic import get_speed

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
chat_id = os.getenv("chat_id")

bot = aiogram.Bot(BOT_TOKEN)
dp = aiogram.Dispatcher()


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
    
