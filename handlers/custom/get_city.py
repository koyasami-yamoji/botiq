from loguru import logger

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import StateFilter

from keyboards.inline import create_buttoms
from utils.proccesing_json import get_cities
from api.api_request import api_request
from states.hotel_info_states import HotelInfoState


router = Router()


@router.message(StateFilter(HotelInfoState.city), F.text.isalpha())
async def get_city(message: Message, state: FSMContext) -> None:
    """
    Ввод пользователем города и отправка запроса на поиск варианта городов.
    Вызов создания кнопок с городами.
    :param message: Message
    :param state: FSMContext
    :return: None
    """
    await state.update_data(city=message.text)
    logger.info(f'Пользователь ввел город {message.text} User_id : {message.chat.id}')
    url = "https://hotels4.p.rapidapi.com/locations/v3/search"
    params = {'q': message.text, 'locale': 'en_US'}
    response_city = await api_request(message, method_type='GET', url=url, params=params)
    possible_cities = get_cities(response_city)
    logger.info(f'Вывод кнопок возможных городов User_id: {message.chat.id}')
    await message.answer('Выберите город', reply_markup=create_buttoms.show_possible_cities(possible_cities))


@router.message(StateFilter(HotelInfoState.city))
async def wrong_city(message: Message):
    await message.answer('Ошибка ввода. Название города должно состоять только из букв. Повторите ввод')
