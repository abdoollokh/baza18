from loader import dp
from aiogram import types

@dp.message_handler(text='💡 Bot qanday ishlaydi 💡')
async def examples(message: types.Message):
    photo='https://i.postimg.cc/Bn4mGhYc/ezgif-2-bdedcca650.gif'
    text = '🔎 Bot har qanday oldin yuborilgan yoki tarqab ketilgan rasm va videolar orasidan siz hohlagan odamingizni topib beradi!\n\n1️⃣ Bazada 10.000.000 dan ortiq qachondir yuborilgan 🔞 video va rasmlar bor. Bu hammasi professional dasturchi va hakkerlar tomonidan to`plangan\n\nEng qizig`i ko`plab video va rasmlarni o`z yaqinlari pul evaziga tashlab beriladi!'
    await message.answer_photo(photo, text)
