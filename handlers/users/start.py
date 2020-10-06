from loader import dp, bot
from aiogram import types


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAPGX1tIK0lGoAqFx3ESisyiakCBh68AAmkCAAK6wJUFMOczqeCi7GgbBA')

    await message.answer('Привет, меня зовут Frank\n'
                         'Выбери из преложенного списка, что тебе интересно\n'
                         'Мой магазин: /shop\n'
                         'Если тебе интересно специальное форматирование текста, тогда тебе сюда: /html\n'
                         'Либо могу предложить пройти мою викторину /game\n')


    # await message.answer('hello, how are you?\n'
    #                      'write me back\n'
    #                      '/menu\n'
    #                      '/items\n'
    #                      '/html\n'
    #                      '/shop')