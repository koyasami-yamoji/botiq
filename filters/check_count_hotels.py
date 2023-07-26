from aiogram.filters import Filter
from aiogram.types import Message


class CountHotelsFilter(Filter):
	async def __call__(self, message: Message):
		return message.text.isdigit() and 0 < int(message.text) <= 25