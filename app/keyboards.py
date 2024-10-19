from gc import callbacks

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)

main = InlineKeyboardMarkup(inline_keyboard=[

    [InlineKeyboardButton(text='Добавить', callback_data='add_to_list'), InlineKeyboardButton(text='Удалить', callback_data='delete_to_list')],
    [InlineKeyboardButton(text='Мой список', callback_data='my_list')]
])

startkb = InlineKeyboardMarkup(inline_keyboard=[

    [InlineKeyboardButton(text='Начнем', callback_data='startkb')]
])
















main2 = ReplyKeyboardMarkup(keyboard=[

    [KeyboardButton(text='Добавить'), KeyboardButton(text='Удалить')],
    [KeyboardButton(text='Мой список')]
],
    resize_keyboard=True, #маленький размер
    input_field_placeholder='Что-то новенькое?') #текст в поле ввода