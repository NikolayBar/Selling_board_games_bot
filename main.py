import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

from config import *
from keyboards import *
from text import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(msg_):
    await msg_.answer(t_start, reply_markup=start_kb)

@dp.message_handler(text='О нас')
async def price(msg_):
    await msg_.answer(t_about, reply_markup=start_kb)

@dp.message_handler(text= 'Стоимость')
async def info(msg_):
    await msg_.answer('Что интересует?', reply_markup=catalog_kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)