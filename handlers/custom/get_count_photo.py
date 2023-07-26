from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import StateFilter

from loguru import logger

from filters import CountPhotoFilter
from states.hotel_info_states import HotelInfoState
from utils.create_calendar import my_calendar

router = Router()


@router.message(StateFilter(HotelInfoState.count_photo), CountPhotoFilter(0, 10))
async def get_count_photo(message: Message, state: FSMContext) -> None:
    """
        Ввод пользователем кол-во фотографий и проверка ввода на число.
        Вызов и создания кнопок с календарем с датой заезда
        :param state: FSMContext
        :param message: Message
        :return: None
        """
    logger.info(f'Ввод пользователем и запись количества фотографий'
                f' {message.text} User_id {message.chat.id}')
    await state.update_data(count_photo=message.text)
    await my_calendar(message, 'заезда')


@router.message(StateFilter(HotelInfoState.count_photo))
async def wrong_count_photo(message: Message):
    await message.answer('Ошибка ввода. Введите число.')