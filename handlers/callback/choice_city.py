from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from loguru import logger

from states import hotel_info_states

router = Router()


@router.callback_query(F.data.isdigit())
async def choice_city(call: CallbackQuery, state: FSMContext) -> None:
	logger.info(f'Пользователь выбрал город. User_id {call.message.chat.id} Id Города {call.data}')
	await state.update_data(destination_id=call.data)
	await call.message.delete()
	await state.set_state(hotel_info_states.HotelInfoState.count_hotels)
	await call.message.answer('Сколько отелей вывести в чат? (не больше 25)')