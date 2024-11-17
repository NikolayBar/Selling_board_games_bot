import texts.t_start
from keyboards import *
import db

async def start(msg_):
    await msg_.answer(f'Добро пожаловать {msg_.from_user.first_name}!\n' + texts.t_start.t_start, reply_markup=start_kb)

async def about_us(msg_):
    with open('media/pic_01.jpg', 'rb') as img:
        await msg_.answer_photo(img, texts.t_start.t_about, reply_markup=start_kb)