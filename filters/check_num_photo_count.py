from aiogram.filters import Filter
from aiogram.types import Message


class CountPhotoFilter(Filter):
	def __init__(self, min_count, max_count):
		self.min_count = min_count
		self.max_count = max_count

	async def __call__(self, message: Message):
		return message.text.isdigit() and self.min_count < int(message.text) <= self.max_count