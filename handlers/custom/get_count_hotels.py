from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import StateFilter

from loguru import logger

from states.hotel_info_states import HotelInfoState
from keyboards.inline.create_buttoms import need_for_photo
from filters import CountHotelsFilter


router = Router()


@router.message(StateFilter(HotelInfoState.count_hotels), CountHotelsFilter())
async def input_count_hotels(message: Message, state: FSMContext) -> None:
    logger.info(f'Ввод пользователем и запись количества отелей в поиске '
                f' {message.text} User_id {message.chat.id}')
    await state.update_data(count_hotels=message.text)
    data = await state.get_data()
    await message.answer('Нужны ли фотографии отеля', reply_markup=need_for_photo())


@router.message(StateFilter(HotelInfoState.count_hotels))
async def wrong_count_hotels(message: Message):
    await message.answer('Ошибка ввода. Число не может быть меньше 0 и больше 25, повторите ввод.')