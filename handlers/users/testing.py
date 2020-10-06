from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Test


@dp.message_handler(Command("test"))
async def test(message: types.Message):
    await message.answer("Вы начали тестировани\n"
                         "Вопрос №1\n"
                         "Вам нравятся яблоки?")


    await Test.Q1.set()
    # await Test.first()


@dp.message_handler(state=Test.Q1)
async def answerq1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    # async with state.proxy() as data:
    #   data["answer1"] = answer
    #   data["list"].append(1)

    # await state.update_data( {"answer1": answer} )

 #-----------------------------------------------------------------------

    await message.answer("Вопрос №2\n"
                         "А груши ты любишь?")
    # await Test.Q2.set()
    await Test.next()

    @dp.message_handler(state=Test.Q2)
    async def answerq2(message: types.Message, state: FSMContext):
        data = await state.get_data()
        answer1 = data.get("answer1")
        answer2 = message.text


        await message.answer("Спасибо за ваши ответы")
        await message.answer(f"Ответ 1: {answer1}")
        await message.answer(f"Ответ 2: {answer2}")


        await state.finish()
        # await state.reset_state(with_data=False)