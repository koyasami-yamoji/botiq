from aiogram.filters.callback_data import CallbackData


class CalendarCallback(CallbackData, prefix='cal'):
	action: str
	year: str
	month: str
	day: str

