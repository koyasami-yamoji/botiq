from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Hotels, History


async def set_record_hotels(hotels: dict, record_history: History, session: AsyncSession) -> list[Hotels]:
	recorded_hotels = []
	for hotel in hotels.values():
		record_hotels = Hotels()
		record_hotels.history_id = record_history.id
		record_hotels.hotel_id = int(hotel['id'])
		record_hotels.name = hotel['name']
		record_hotels.price = float(hotel['price'])
		record_hotels.distance = float(hotel['distance'])
		record_hotels.address = hotel['address']
		if hotel.get('user_rates'):
			record_hotels.user_rates = hotel['user_rates']
		session.add(record_hotels)
		recorded_hotels.append(record_hotels)
	await session.commit()
	return recorded_hotels