from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext


def need_for_photo():
    builder = InlineKeyboardBuilder()
    builder.button(text='Да', callback_data='да')
    builder.button(text='Нет', callback_data='нет')
    return builder.as_markup()


def show_possible_cities(possible_cities: dict):
    builder = InlineKeyboardBuilder()
    for key, value in possible_cities.items():
        builder.button(text=value['regionNames'], callback_data=value['gaiaId'])
    return builder.as_markup()

