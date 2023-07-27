from sqlalchemy.orm import Session
from db.models import Hotels, History


def set_hotels(hotels: dict, record_history: History, session: Session) -> list[Hotels]:
	recorded_hotels = []
	for hotel in hotels.values():
		record_hotels = Hotels()
		record_hotels.history_id = record_history.id
		record_hotels.hotel_id = hotel['id']
		record_hotels.address = hotel['address']
		record_hotels.name = hotel['name']
		record_hotels.price = hotel['price']
		record_hotels.user_rates = hotel['user_rates']
		record_hotels.images = hotel['images']
		record_hotels.distance = hotel['distance']
		session.add(record_hotels)
		recorded_hotels.append(record_hotels)
	session.commit()

	return recorded_hotels