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
from admin import *
from db import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(msg_):
    await msg_.answer(f'Добро пожаловать {msg_.from_user.first_name}!\n' + t_start, reply_markup=start_kb)


@dp.message_handler(text='О нас')
async def price(msg_):
    with open('files/pic_01.jpg', 'rb') as img:
        await msg_.answer_photo(img, t_about, reply_markup=start_kb)


@dp.message_handler(text='Стоимость')
async def info(msg_):
    await msg_.answer('Что интересует?', reply_markup=catalog_kb)


@dp.callback_query_handler(text='medium')
async def buy_m(call):
    with open('files/pic_02.jpg', 'rb') as img:
        await call.message.answer_photo(img, t_M_game, reply_markup=buy_kb)
        await call.answer()


@dp.callback_query_handler(text='big')
async def buy_l(call):
    with open('files/pic_03.jpg', 'rb') as img:
        await call.message.answer_photo(img, t_L_game, reply_markup=buy_kb)
        await call.answer()


@dp.callback_query_handler(text='mega')
async def buy_xl(call):
    with open('files/pic_04.jpg', 'rb') as img:
        await call.message.answer_photo(img, t_XL_game, reply_markup=buy_kb)
        await call.answer()


@dp.callback_query_handler(text='other')
async def buy_other(call):
    await call.message.answer(text=t_other)
    await call.answer()


@dp.callback_query_handler(text='back_to_catalog')
async def back(call):
    await call.message.answer('Что интересует?', reply_markup=catalog_kb)
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
