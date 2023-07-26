import datetime

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from loguru import logger

from states import hotel_info_states

router = Router()


@router.message(Command(commands=['lower', 'higher', 'custom']))
async def input_command(message: Message, state: FSMContext) -> None:
    """
    Обработчик введенной пользователем команды. "custom, lower, higher"
    И запоминаем нужные данные.
    Спрашивает пользователя какой искать город.
    :param state: FSMContext
    :param message: Message
    :return: None
    """
    logger.info(f'Пользователь ввел команду {message.text}, User_id {message.chat.id}')
    sort = check_command(message.text)
    await state.update_data(command=message.text,
                            chat_id=message.chat.id,
                            date_time=datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
                            sort=sort)
    await state.set_state(hotel_info_states.HotelInfoState.city)
    await message.answer("Введите город в котором хотите найти отель (На латинице)")


def check_command(command: str) -> str:
    """
    Проверка команды и назначение параметра сортировки
    : param command : str команда, выбранная (введенная) пользователем
    : return : str команда сортировки
    """
    sort = {
        '/custom': 'DISTANCE',
        '/lower': 'PRICE_LOW_TO_HIGH',
        '/higher': 'PRICE_LOW_TO_HIGH'
    }
    return sort[command]