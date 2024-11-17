import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

from config import *
from keyboards import *
from admin import *
from db import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

import handlers.start
import handlers.catalog

dp.message_handler(commands=['start'])(handlers.start.start)

dp.message_handler(Text(equals=['О нас']))(handlers.start.about_us)
dp.message_handler(Text(equals=['Стоимость']))(handlers.catalog.info)

dp.callback_query_handler(text='medium')(handlers.catalog.buy_m)

dp.callback_query_handler(text='big')(handlers.catalog.buy_l)

dp.callback_query_handler(text='mega')(handlers.catalog.buy_xl)

dp.callback_query_handler(text='other')(handlers.catalog.buy_other)

dp.callback_query_handler(text='back_to_catalog')(handlers.catalog.back)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
