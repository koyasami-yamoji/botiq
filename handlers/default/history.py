from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession

from db.get_from_db.get_history_from_db import get_history_from_db
from db.get_from_db.get_hotels_from_db import get_hotels
from utils.create_messages.create_history_message import history_message
from utils.create_messages.create_hotel_message_from_db import hotel_from_db_message

router = Router()


@router.message(Command('history'))
async def get_history(message: Message, session: AsyncSession) -> None:
	history_records = await get_history_from_db(message.chat.id, session)
	if not history_records:
		await message.answer('Историй поиска не найдено.')
		return
	for record in history_records:
		await message.answer(text=history_message(record), disable_web_page_preview=True)
		hotels = await get_hotels(record, session)
		for hotel in hotels:
			print(hotel)
			await message.answer(text=hotel_from_db_message(hotel[0]), disable_web_page_preview=True)
