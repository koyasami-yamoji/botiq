
from utils.create_calendar import my_calendar
from keyboards.inline.calendar.calendar import Calendar, check_month_day
from loguru import logger
from states.hotel_info_states import HotelInfoState
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from api.find_hotel import find_hotel

from filters import CalendarCallback


calendar = Calendar()
router = Router()


@router.callback_query(CalendarCallback.filter((F.action == 'PREV-MONTH') | (F.action == 'NEXT-MONTH')))
async def change_month(call: CallbackQuery, callback_data: CalendarCallback):
    action = callback_data.action
    year = callback_data.year
    month = callback_data.month
    day = callback_data.day
    await calendar.calendar_query_handler(call=call, action=action, year=year, month=month, day=day)


@router.callback_query(StateFilter(HotelInfoState.out_date), CalendarCallback.filter(F.action == 'DAY'))
async def select_out_date(call: CallbackQuery, state: FSMContext, callback_data: CalendarCallback):
    year = callback_data.year
    month = callback_data.month
    day = callback_data.day
    data = await state.get_data()
    date_out = int(year + check_month_day(month) + check_month_day(day))
    date_in = int(data['CheckInDate']['year'] + check_month_day(data['CheckInDate']['month']) +
                  check_month_day(data['CheckInDate']['day']))

    if date_out > date_in:
        logger.info(f'Ввод и сохранения даты выезда пользователем {call.message.chat.id}')
        await state.update_data(CheckOutDate={'day': day, 'month': month, 'year': year}, min_distance=0, max_distance=0)
        await call.message.delete()

        if data['sort'] == 'DISTANCE':
            await state.set_state(HotelInfoState.min_price)
            await call.message.answer('Введите минимальную стоимость отела за сутки (В долларах Сша)')

        else:
            data = await state.get_data()
            await find_hotel(message=call.message, data=data)
    else:
        await call.message.answer('Дата выезда должна быть больше даты заезда')
        await call.message.delete()
        await my_calendar(call.message, 'выезда')


@router.callback_query(CalendarCallback.filter(F.action == 'DAY'))
async def select_date(call: CallbackQuery, state: FSMContext, callback_data: CalendarCallback):
    year = callback_data.year
    month = callback_data.month
    day = callback_data.day
    logger.info(f'Выбрана дата заезда {year}:{month}:{day} . User_id: {call.message.chat.id}')
    await state.update_data(CheckInDate={'day': day, 'month': month, 'year': year})
    await call.message.delete()
    await state.set_state(HotelInfoState.out_date)
    await my_calendar(call.message, 'выезда')









# @router.callback_query(CalendarCallback.filter(F.action == 'DAY'))
# async def select_date(call: CallbackQuery, state: FSMContext, callback_data: CalendarCallback):
# 	year = callback_data.year
# 	month = callback_data.month
# 	day = callback_data.day
#
# 	await state.set_state(HotelInfoState.input_date)
# 	data = await state.get_data()
# 	logger.info(f'Выбрана дата пользователем, проверяем User_id: {call.message.chat.id}')
# 	select_date_ = year + check_month_day(month) + check_month_day(day)
#
# 	if 'CheckInDate' in data:
# 		checkin = int(data['CheckInDate']['year'] + data['CheckInDate']['month'] + data['CheckInDate']['day'])
#
# 		if int(select_date_) > checkin:
# 			logger.info(f'Ввод и сохранения даты выезда пользователем {call.message.chat.id}')
# 			await state.update_data(CheckOutDate={'day': day, 'month': month, 'year': year})
# 			await state.update_data(min_distance=0)
# 			await state.update_data(max_distance=0)
# 			await call.message.delete()
#
# 			if data['sort'] == 'DISTANCE':
# 				await state.set_state(HotelInfoState.min_price)
# 				await call.message.answer('Введите минимальную стоимость отела за сутки (В долларах Сша)')
#
# 			else:
# 				await find_hotel(message=call.message, data=data)
#
# 		else:
# 			await call.message.answer('Дата выезда должна быть больше даты заезда')
# 			await call.message.delete()
# 			await my_calendar(call.message, 'выезда')
# 	else:
# 		logger.info(f'Ввод и сохранения даты заезда пользователем User_id {call.message.chat.id}')
# 		await state.update_data(CheckInDate={'day': day, 'month': month, 'year': year})
# 		await call.message.delete()
# 		await my_calendar(call.message, 'выезда')


