from loader import bot, dp
from aiogram import types
from utils import database
import json
from states.widthraw_request import Widthdraw
from aiogram.dispatcher.storage import FSMContext

@dp.message_handler(commands=['pay'])
async def widthdraw(message: types.Message):
    user_data = database.get_user(message.from_user.id)
    balance = user_data['balance']
    if int(balance) == 0:
        await message.answer('<b>Sizning xisobingiz 0₽, siz pul chiqara olmaysiz.</b>')
    else:
        await message.answer(f'<b>Pulni qayerga yuborishimizni tanlang...</b>')
        await Widthdraw.waiting_comment.set()

@dp.message_handler(state=Widthdraw.waiting_comment)
async def add_comment(message: types.Message, state: FSMContext):
    await message.answer('<b>Arizangiz qabul qilindi!</b>')
    user_data = database.get_user(message.from_user.id)
    balance = user_data['balance']
    database.update_user(message.from_user.id, 'balance', 0)
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    for admin in config['Bot_Data']['Admins']:
        try:
            await bot.send_message(admin, f'User: @{message.from_user.username} | ({message.from_user.id})\n\nChiqariladigon pul miqdori: {balance} RUB!\n\nRekvizit:\n{message.text}')
        except:
            pass
    await state.finish()
