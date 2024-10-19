from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

main_menu=ReplyKeyboardMarkup(resize_keyboard=True)

add_car=KeyboardButton(text='Add Car')
buy_car=KeyboardButton(text='Buy Car')

main_menu.add(add_car)
main_menu.add(buy_car)