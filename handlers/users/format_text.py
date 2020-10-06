from aiogram import types
from loader import dp

from aiogram.utils.markdown import hbold, hcode, hitalic, hunderline, hlink, hstrikethrough
from aiogram.dispatcher.filters import Command


html_text = "\n".join(
    [
        "Hello, " + hbold("my friend"),
         hitalic("What is your favorite color?"),
        ""
        "Don't choose this " + hstrikethrough("ABC"),
        "Buy water " + hlink("here", "https://www.apple.com/ru/"),
         hunderline("Attention"),
         "",
         hcode("example")
    ]
)

html_text += hcode(html_text)

@dp.message_handler(Command("html"))
async def show_html(message: types.Message):
    await message.answer(html_text, parse_mode=types.ParseMode.HTML)