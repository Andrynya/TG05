import asyncio
import logging
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart
from config import TOKEN

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создаем экземпляры бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def get_random_trivia():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://numbersapi.com/random/trivia') as response:
            if response.status == 200:
                return await response.text()
            else:
                return "Ошибка получения факта."

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.reply("Привет! Напиши /trivia, чтобы получить случайный факт о числе.")

@dp.message(Command('trivia'))
async def trivia(message: types.Message):
    trivia = await get_random_trivia()
    await message.reply(trivia)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
