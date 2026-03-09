import requests
import os
import aiogram
from aiogram.types import Message
from aiogram.filters import Command
import asyncio
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = aiogram.Bot(BOT_TOKEN)
dp = aiogram.Dispatcher()
chat_id = 1648413619

@dp.message(Command(commands='traffic'))
async def send_traffic(message: Message):
    with open("../jsonOutput.txt", "r", encoding="utf-8") as users:
        await message.answer(users.read())

def read_ips() -> str:
    with open("ips.txt", 'r', encoding="utf-8") as ips:
        text = ips.read()
    return text

@dp.message(Command(commands='ips'))
async def send_ip(message: Message):
    text = read_ips()
    await message.answer(text)

async def send_ips_cycle():
    while True:
        text = read_ips()
        await bot.send_message(1648413619, text)
        await asyncio.sleep(21600)
           	


async def main():
    asyncio.create_task(send_ips_cycle())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
