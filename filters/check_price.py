from aiogram.filters import Filter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


class MinPriceFilter(Filter):

	async def __call__(self, message: Message) -> bool:
		return message.text.isdigit() and int(message.text) > 0


class MaxPriceFilter(Filter):

	async def __call__(self, message: Message, state: FSMContext) -> bool:
		data = await state.get_data()
		return message.text.isdigit() and int(message.text) > int(data['min_price'])



