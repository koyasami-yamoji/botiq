from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from loguru import logger
from states import hotel_info_states

#TODO: ДОПИСАТЬ ТУТ КАЛЕНДАРЬ

router = Router()


@router.callback_query(Text(text=['да']))
async def need_photo_callback(callback: CallbackQuery, state: FSMContext):
    logger.info(f'Пользователь нажал "да" user_id {callback.message.chat.id}')
    await state.update_data(need_photo=callback.data)
    await state.set_state(hotel_info_states.HotelInfoState.count_photo)
    await callback.answer('Введите кол-во фотографий (не больше 10)')


@router.callback_query(Text(text=['нет']))
async def need_photo_callback(callback: CallbackQuery, state: FSMContext):
    logger.info(f'Пользователь нажал "нет" user_id {callback.message.chat.id}')
    await state.update_data(need_photo=callback.data, count_photo=0)
