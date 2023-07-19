from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def need_for_photo():
    builder = InlineKeyboardBuilder()
    builder.button(text='Да', callback_data='да')
    builder.button(text='Нет', callback_data='нет')
    return builder.as_markup()





