from loader import dp,bot,zalety
from aiogram import types
from keyboards import social_check_keyboard
from utils import database



@dp.message_handler(text='🔍 Bazadan qidirish 🔍')
async def find_leaks(message: types.Message):
    text=f'''👋 Привет, {message.from_user.full_name}\n\nBu bot har qanda qizning ijtimoiy tarmoqdagi profillari orqali shaxsiy ma`lumotlarini, yoki 🔞 rasm, videolarini topib beradi  😏\n\n🔎 Botga Instagram, Vkontakte yoki Telefon raqamni (Whatsapp, Telegram, Viberdan qidirsh uchun) yuboring  🔞👇'''
    photo='https://sun9-18.userapi.com/impg/3xn4BHggsVfxVb55sLbXOVDgNVqJE0t_pbchbw/f4Zkc6MgZSU.jpg?size=640x640&quality=95&sign=e6f8c1e2180063b2d5984c33428a28b8&type=album'
    await message.answer_photo(photo, text)
    await message.answer('🔥 Qayerdan izlashimizni tanlang', reply_markup=social_check_keyboard.keyboard)

@dp.callback_query_handler(text='instagram')
async def inst(callback: types.CallbackQuery):
    await callback.message.edit_text('<b>Instagram ssilkasini yuboring</b>\n\nBunday shaklda:\nhttps://www.instagram.com/karna.val/\ninstagram.com/samoylovaoxana/', reply_markup=social_check_keyboard.back_keyboard)

@dp.callback_query_handler(text='vk')
async def inst(callback: types.CallbackQuery):
    await callback.message.edit_text('<b>Vkontakte ssilkasini yuboring</b>\n\nBunday shaklda:\nhttps://vk.com/id494445129\nvk.com/id173811890', reply_markup=social_check_keyboard.back_keyboard)

@dp.callback_query_handler(text='phone_number')
async def inst(callback: types.CallbackQuery):
    await callback.message.edit_text('<b>Telefon raqamini + bilan boshlangan shaklda yuboring</b>\n\n+7...\n+998...', reply_markup=social_check_keyboard.back_keyboard)

@dp.callback_query_handler(text='tiktok')
async def inst(callback: types.CallbackQuery):
    await callback.message.edit_text('<b>Usernamesini yuboring</b>\n\nBunday shaklda:\n@karinakross\n@buzova86', reply_markup=social_check_keyboard.back_keyboard)

@dp.callback_query_handler(text='social_back')
async def back(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🔥 Qayerdan izlashimizni tanlang', reply_markup=social_check_keyboard.keyboard)