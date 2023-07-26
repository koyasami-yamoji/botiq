from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from filters import MinPriceFilter, MaxPriceFilter
from loguru import logger

from states.hotel_info_states import HotelInfoState


router = Router()


@router.message(StateFilter(HotelInfoState.min_price), MinPriceFilter())
async def get_min_price(message: Message, state: FSMContext) -> None:
	logger.info(f'Ввод пользователем и запись минимальной цены за отель '
				f'{message.text} User_id {message.chat.id}')
	await state.update_data(min_price=message.text)
	await state.set_state(HotelInfoState.max_price)
	await message.answer('Введите максимальную стоимость за сутки в отеле в долларах (США)')


@router.message(StateFilter(HotelInfoState.min_price))
async def wrong_min_price(message: Message):
	await message.answer('Ошибка ввода. Стоимость может состоять только из цифр и не может быть меньше нуля! '
						 'Повторите ввод.')


@router.message(StateFilter(HotelInfoState.max_price), MaxPriceFilter())
async def get_max_price(message: Message, state: FSMContext) -> None:
	logger.info(f'Ввод пользователем и запись максимальной цены за отель '
				f'{message.text} User_id {message.chat.id}')
	await state.update_data(max_price=message.text)
	await state.set_state(HotelInfoState.min_distance_to_center)
	await message.answer('Введите минимальное расстояние отеля до центра (Км)')


@router.message(StateFilter(HotelInfoState.max_price))
async def wrong_max_price(message: Message):
	await message.answer('Ошибка ввода. Максимальная цена должна состоять из цифр и быть больше минимальной цены! '
						 'Повторите ввод.')
