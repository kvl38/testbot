from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboard.default.knopki import friends, fruits
from loader import dp, bot


@dp.message_handler(Command('game'))
async def first(message: types.Message):
    # bot.send_sticker(chat_id=message.chat.id,CAACAgIAAxkBAAPGX1tIK0lGoAqFx3ESisyiakCBh68AAmkCAAK6wJUFMOczqeCi7GgbBA)

    await message.answer('О ты захотел поиграть. Удачи тебе...')

    await message.answer('1-й вопрос: кто из твоих друзей прыгал с крыши?',reply_markup=friends)

@dp.message_handler(text="Надя")
async def orange(message: types.Message):
    await message.answer("Ты ответил верно!!! Это была Надюха", reply_markup=ReplyKeyboardRemove())
    await message.answer('2-й вопрос: Что ты больше любишь?', reply_markup=fruits)

@dp.message_handler(Text(equals=["Юра","Алина","Артем","Даша","Паша"]))
async def apples(message: types.Message):
    await message.answer(f"Ты выбрал {message.text}\n"
                         f"Фигово ты друзей знаешь, попробуй еще раз")

@dp.message_handler(text="Яблоки")
async def g(message: types.Message):
    await message.answer("Поздравляю, у тебя хороший вкус!!!", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Text(equals=["Бананы","Апельсины"]))
async def ok(message: types.Message):
    await message.answer(f"Ты выбрал {message.text}\n"
                         f"Немного не то, что я хотел, выбери другой фрукт!!!")

