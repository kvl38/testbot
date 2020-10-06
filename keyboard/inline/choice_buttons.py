from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboard.inline.callback_datas import buy_callback

from emoji import emojize
choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="Купить грушу", callback_data=buy_callback.new(item_name="pear", quantity=1))
choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="Купить яблоки", callback_data="buy:apple:5")
choice.insert(buy_apples)

cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
choice.insert(cancel_button)


apple_keyboard = InlineKeyboardMarkup()
APPLE_LINK = "https://www.apple.com/ru/"
apple_link = InlineKeyboardButton(text="Купи тут", url=APPLE_LINK)
apple_keyboard.insert(apple_link)


items = InlineKeyboardMarkup(row_width=2)
fruits = InlineKeyboardButton(text="Фрукты 🍏", callback_data=buy_callback.new(item_name="fruits", quantity=4))
items.insert(fruits)
stocks = InlineKeyboardButton(text="Акции 💵", callback_data="buy:stocks:6")
items.insert(stocks)
device = InlineKeyboardButton(text="Устройства 📲", callback_data="buy:device:2")
items.insert(device)
cars = InlineKeyboardButton(text="Машины 🚗", callback_data="buy:cars:3")
items.insert(cars)


device_keyboard = InlineKeyboardMarkup(row_width=2)
iphone = InlineKeyboardButton(text="iphone Xs 📱", callback_data="buy:iphone:5",url='https://www.apple.com/shop/buy-iphone/iphone-xr')
device_keyboard.insert(iphone)
macbook = InlineKeyboardButton(text="MacBook Pro 💻", callback_data="buy:macbook:3",url='https://www.apple.com/shop/buy-mac/macbook-pro/13-inch')
device_keyboard.insert(macbook)