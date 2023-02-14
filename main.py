from aiogram import types, Dispatcher, Bot, executor
from api import weather
from environs import Env

env = Env()
env.read_env()

token = env.str('token')

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}! Wikipedia botga ma'lumot kiriting")


@dp.message_handler(content_types='text')
async def wikipedia(message: types.Message):
    text = message.text
    result = wiki(text)
    await message.answer(result)


if __name__ == '__main__':
    executor.start_polling(dp)
