from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher



from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

photo1 = 'AgACAgIAAxkBAAIBgV9iZpM-YSy_OWcbL1ftSU8ngnUTAAKjsTEbnj8QS8dj1mVgDfAx2A5Ili4AAwEAAwIAA20AAy8BAgABGwQ'
KITTENS = [
    'AgACAgIAAxkBAAIBgV9iZpM-YSy_OWcbL1ftSU8ngnUTAAKjsTEbnj8QS8dj1mVgDfAx2A5Ili4AAwEAAwIAA20AAy8BAgABGwQ',
    'AgACAgIAAxkBAAIBgV9iZpM-YSy_OWcbL1ftSU8ngnUTAAKjsTEbnj8QS8dj1mVgDfAx2A5Ili4AAwEAAwIAA20AAy8BAgABGwQ',
    'AgACAgIAAxkBAAIBgV9iZpM-YSy_OWcbL1ftSU8ngnUTAAKjsTEbnj8QS8dj1mVgDfAx2A5Ili4AAwEAAwIAA20AAy8BAgABGwQ',
]
VOICE = 'AwACAgIAAxkBAAIBil9iaFIUY5HxWZuculQL1smEEdBSAAIFCwACnj8QS6WVb-kEsWguGwQ'
# VIDEO = 'BAADAgADXAEAAnhu6ErDHE-xNjIzMgI'
# TEXT_FILE = 'BQADAgADWgEAAnhu6ErgyjSYkwOL6AI'
# VIDEO_NOTE = 'DQADAgADWwEAAnhu6EoFqDa-fStSmgI'


@dp.message_handler(commands=['start'])
async def privet(message: types.Message):
    await message.reply(text('Hi, how are you?'
                        'Write me back:\n'
                        '/voice', '/photo', '/group', '/note', '/file','/echo',sep='\n'))

@dp.message_handler(content_types=['voice'])
async def sticker_id(message):
    print(message)

# @dp.message_handler(commands=['help'])
# async def help_command(message: types.Message):
#     msg = text(bold('Я могу ответить на следующие команды:'),
#                '/voice', '/photo', '/group', '/note', '/file, /testpre', sep='\n')
#     await message.reply(msg, parse_mode=ParseMode.MARKDOWN)
#
# @dp.message_handler(commands=['voice'])
# async def voice_command(message: types.Message):
#     await bot.send_voice(message.from_user.id, VOICE,
#                          reply_to_message_id=message.message_id)
#
#
# @dp.message_handler(commands=['photo'])
# async def photo_command(message: types.Message):
#     caption = 'Какие глазки! :eyes:'
#     await bot.send_photo(message.from_user.id, photo1,
#                          caption=emojize(caption),
#                          reply_to_message_id=message.message_id)
#
#
# @dp.message_handler(commands=['group'])
# async def group_command(message: types.Message):
#     media = [InputMediaVideo(VIDEO, 'миньёны!!!')]
#     for photo_id in KITTENS:
#         media.append(InputMediaPhoto(photo_id))
#     await bot.send_media_group(message.from_user.id, media)
#
#
# @dp.message_handler(commands=['note'])
# async def note_command(message: types.Message):
#     user_id = message.from_user.id
#     await bot.send_chat_action(user_id, ChatActions.RECORD_VIDEO_NOTE)
#     await asyncio.sleep(1)  # конвертируем видео и отправляем его пользователю
#     await bot.send_video_note(message.from_user.id, VIDEO_NOTE)
#
#
# @dp.message_handler(commands=['file'])
# async def file_command(message: types.Message):
#     user_id = message.from_user.id
#     await bot.send_chat_action(user_id, ChatActions.UPLOAD_DOCUMENT)
#     await asyncio.sleep(1)  # скачиваем файл и отправляем его пользователю
#     await bot.send_document(user_id, TEXT_FILE,
#                             caption='Этот файл специально для тебя!')
#
#
# @dp.message_handler(commands=['testpre'])
# async def testpre_command(message: types.Message):
#     message_text = pre(emojize('''@dp.message_handler(commands=['testpre'])
#     async def process_testpre_command(message: types.Message):
#     message_text = pre(emojize('Ха! Не в этот раз :smirk:'))
#     await bot.send_message(message.from_user.id, message_text)'''))
#     await bot.send_message(message.from_user.id, message_text,
#                            parse_mode=ParseMode.MARKDOWN)
#
#
# @dp.message_handler(commands=['echo'])
# async def echo_msg(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)

