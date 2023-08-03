from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from loguru import logger

from states import hotel_info_states
from utils.create_calendar import my_calendar


router = Router()


@router.callback_query(F.data.in_({'да', 'нет'}))
async def need_photo_callback(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'да':
        logger.info(f'Пользователь нажал "да" user_id {callback.message.chat.id}')
        await state.update_data(need_photo=callback.data)
        await state.set_state(hotel_info_states.HotelInfoState.count_photo)
        await callback.message.delete()
        await callback.message.answer('Введите кол-во фотографий (не больше 10)')
    else:
        logger.info(f'Пользователь нажал "нет" user_id {callback.message.chat.id}')
        await state.update_data(need_photo=callback.data, count_photo=0)
        await callback.message.delete()
        await my_calendar(message=callback.message, word='заезда')

