from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from loguru import logger

from api.find_hotel import find_hotel
from states.hotel_info_states import HotelInfoState
from filters.check_distance import CheckNumDistance

router = Router()


@router.message(StateFilter(HotelInfoState.min_distance_to_center), CheckNumDistance())
async def get_min_distance_to_center(message: Message, state: FSMContext):
	logger.info(f'Ввод пользователем и запись минимального расстояния отеля до центра '
				f'{message.text} User_id {message.chat.id}')
	await state.update_data(min_distance=message.text)
	await state.set_state(HotelInfoState.max_distance_to_center)
	await message.answer('Введите максимальное расстояние отеля до центра')


@router.message(StateFilter(HotelInfoState.min_distance_to_center))
async def wrong_min_distance(message: Message):
	await message.answer('Ошибка ввода. Введите число.')


@router.message(StateFilter(HotelInfoState.max_distance_to_center), CheckNumDistance())
async def get_max_distance_to_center(message: Message, state: FSMContext):
	logger.info(f'Ввод пользователем и запись максимального расстояния отеля до центра '
				f'{message.text} User_id {message.chat.id}')
	await state.update_data(max_distance=message.text)
	data = await state.get_data()
	await find_hotel(message, data, state)


@router.message(StateFilter(HotelInfoState.max_distance_to_center))
async def wrong_max_distance(message: Message):
	await message.answer('Ошибка ввода. Введите число')
