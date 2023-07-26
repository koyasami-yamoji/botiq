from aiogram.filters import Filter
from aiogram.types import Message


class CheckNumDistance(Filter):
	async def __call__(self, message: Message):
		return message.text.isdigit()