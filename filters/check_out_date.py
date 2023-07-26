# from aiogram.filters import Filter
# from aiogram.types import CallbackQuery
# from aiogram.fsm.context import FSMContext
# from keyboards.inline.calendar.calendar import check_month_day
#
#
# class CheckOutDate(Filter):
# 	def __int__(self, year, month, day):
# 		self.date = year + check_month_day(month) + check_month_day(day)
#
# 	async def __call__(self, call: CallbackQuery,  state: FSMContext = None):
# 		data = await state.get_data()
# 		checkin = int(data['CheckInDate']['year'] + data['CheckInDate']['month'] + data['CheckInDate']['day'])
# 		return self.date > checkin