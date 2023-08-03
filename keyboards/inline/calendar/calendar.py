import datetime
from dataclasses import dataclass
import calendar

from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from filters.callback_filter_factory import CalendarCallback


@dataclass
class Language:
	days: tuple
	months: dict


RUSSIAN_LANGUAGE = Language(
	days=("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"),
	months={
		'January': "Январь",
		'February': "Февраль",
		'March': "Март",
		'April': "Апрель",
		'May': "Май",
		'June': "Июнь",
		'July': "Июль",
		'August': "Август",
		'September': "Сентябрь",
		'October': "Октябрь",
		'November': "Ноябрь",
		'December': "Декабрь"
		}
)


class Calendar:
	__lang = Language

	def __init__(self, language: Language = RUSSIAN_LANGUAGE):
		self.__lang = language

	def create_calendar(self, year=None, month=None):
		now_date = datetime.datetime.now()
		builder = InlineKeyboardBuilder()

		if year is None:
			year = str(now_date.year)
		if month is None:
			month = str(now_date.month)
		else:
			year = str(year)
			month = str(month)

		date_ignore = CalendarCallback(action='IGNORE', year=year, month=month, day="0").pack()

		row = []
		for day in self.__lang.days:
			row.append(InlineKeyboardButton(text=day, callback_data=date_ignore))
		builder.row(*row)

		my_calendar = calendar.monthcalendar(int(year), int(month))
		for week in my_calendar:
			row = []
			for day in week:
				if day == 0:
					row.append(InlineKeyboardButton(text=' ', callback_data=date_ignore))
				else:
					row.append(InlineKeyboardButton(text=str(day), callback_data=
					CalendarCallback(action='DAY', year=year, month=month, day=str(day)).pack()))
			builder.row(*row)

		row = [
			InlineKeyboardButton(text='<--', callback_data=CalendarCallback(action='PREV-MONTH', year=year,
																			month=month, day="0").pack()),
			InlineKeyboardButton(text=self.__lang.months[calendar.month_name[int(month)]] + " " + str(year),
								 callback_data=date_ignore),
			InlineKeyboardButton(text='-->', callback_data=CalendarCallback(action='NEXT-MONTH', year=year, month=month,
																			day="0").pack())
		]
		builder.row(*row)
		return builder.as_markup()

	async def calendar_query_handler(self, call: CallbackQuery, action, year, month, day):
		(action, year, month, day) = (action, year, month, day)
		current_data = datetime.datetime(int(year), int(month), 1)
		if action == 'IGNORE':
			await call.message.answer_callback_query(callback_query_id=call.id)
			return False, None

		elif action == 'PREV-MONTH':
			prev_month = current_data - datetime.timedelta(days=1)
			await call.message.edit_reply_markup(
				reply_markup=self.create_calendar(int(prev_month.year), int(prev_month.month)))
			return None

		elif action == 'NEXT-MONTH':
			next_month = current_data + datetime.timedelta(days=31)
			await call.message.edit_reply_markup(
								  reply_markup=self.create_calendar(int(next_month.year), int(next_month.month)))
			return None

		else:
			await call.message.answer_callback_query(callback_query_id=call.id, text='Что-то пошло не так')
			await call.message.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
			return None


# class CallbackData:
#
# 	@staticmethod
# 	def create_callback_data(action, year, month, day):
# 		return ';'.join([action, str(year), str(month), str(day)])
#
# 	@staticmethod
# 	def separate_data(data):
# 		return data.split(';')


def check_month_day(number: str) -> str:
	"""
	Преобразование формата числа месяца или дня из формата 1..9 в формат 01..09
	: param number : str, число месяца или дня
	: return number : str
	"""
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	if int(number) in numbers:
		number = '0' + number
	return number










