from aiogram.types import InputMediaPhoto

import texts.t_catalog
from keyboards import *

async def info(msg_):
    await msg_.answer('Что интересует?', reply_markup=catalog_kb)

async def buy_m(call):
    with open('media/pic_02.jpg', 'rb') as img:
        await call.message.answer_photo(img, texts.t_catalog.t_M_game, reply_markup=buy_kb)
        await call.answer()

async def buy_l(call):
    with open('media/pic_03.jpg', 'rb') as img:
        await call.message.answer_photo(img, texts.t_catalog.t_L_game, reply_markup=buy_kb)
        await call.answer()

async def buy_xl(call):
    with open('media/pic_04.jpg', 'rb') as img:
        await call.message.answer_photo(img, texts.t_catalog.t_XL_game, reply_markup=buy_kb)
        await call.answer()

async def buy_other(call):
    await call.message.answer(text=texts.t_catalog.t_other)
    await call.answer()

async def back(call):
    await call.message.answer('Что интересует?', reply_markup=catalog_kb)
    await call.answer()