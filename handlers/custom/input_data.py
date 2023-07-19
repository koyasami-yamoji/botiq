import datetime
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from states import hotel_info_states
from aiogram.fsm.context import FSMContext
from loguru import logger
from keyboards.inline import create_buttoms

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
    await state.update_data(command=message.text,
                            chat_id=message.chat.id,
                            date_time=datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
                            sort=check_command(message.text))
    await state.set_state(hotel_info_states.HotelInfoState.city)
    await message.answer("Введите город в котором хотите найти отель (На латинице)")


@router.message(StateFilter(hotel_info_states.HotelInfoState.city), F.text.isalpha())
async def input_city(message: Message, state: FSMContext) -> None:
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
    params = {'q': {message.text}, 'locale': 'en_US'}
    await state.set_state(hotel_info_states.HotelInfoState.count_hotels)  # TODO: сделать проверку на команду
    await message.answer('Введите кол-во отелей')


@router.message(StateFilter(hotel_info_states.HotelInfoState.count_hotels),
                lambda x: x.text.isdigit() and 0 < int(x.text) < 25)
async def input_count_hotels(message: Message, state: FSMContext) -> None:
    logger.info(f'Ввод пользователем и запись количества отелей в поиске '
                f' {message.text} User_id {message.chat.id}')
    await state.update_data(count_hotels=message.text)
    data = await state.get_data()
    if data['sort'] == 'custom':
        await state.set_state(hotel_info_states.HotelInfoState.min_price)
    else:
        await message.answer('Нужны ли фотографии отеля', reply_markup=create_buttoms.need_for_photo())



@router















def check_command(command: str) -> str:
    """
    Проверка команды и назначение параметра сортировки
    : param command : str команда, выбранная (введенная) пользователем
    : return : str команда сортировки
    """
    if command == '/custom':
        return 'DISTANCE'
    elif command == '/lower':
        return 'PRICE_LOW_TO_HIGH'
    elif command == '/higher':
        return 'PRICE_HIGH_TO_LOW'
