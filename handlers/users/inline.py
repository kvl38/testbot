import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboard.inline.callback_datas import buy_callback
from keyboard.inline.choice_buttons import choice, apple_keyboard
from loader import dp, bot


@dp.message_handler(Command("items"))
async def show_items(message: types.Message):
    await message.answer(text="Выберите предмет для покупки\n"
                              "Если вам ничего не надо - нажмите отмену",
                         reply_markup=choice)

@dp.callback_query_handler(buy_callback.filter(item_name="apple"))
async def buying_apple(call: CallbackQuery, callback_data: dict):
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=30)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Вы выбрали купить яблоки. Яблок всего {quantity}. Cпасибо",
                              reply_markup=apple_keyboard)
