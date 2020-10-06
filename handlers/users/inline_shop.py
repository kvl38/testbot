import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboard.inline.callback_datas import buy_callback
from keyboard.inline.choice_buttons import items, device_keyboard
from loader import dp, bot


@dp.message_handler(Command("shop"))
async def show_items(message: types.Message):
    await message.answer(text="Привет, ты зашёл в магазин Franka\n"
                              "Выбери категорию товара, которую хочешь преобрести.",
                         reply_markup=items)


@dp.callback_query_handler(buy_callback.filter(item_name="device"))
async def buying_device(call: CallbackQuery, callback_data: dict):
    await bot.answer_callback_query(callback_query_id=call.id)
    await call.message.answer("Выберите вещь для покупки.",
                              reply_markup=device_keyboard)


