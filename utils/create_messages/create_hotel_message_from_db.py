from db.models import Hotels


def hotel_from_db_message(hotel: Hotels):
	string = f"🏙 Название отеля: {hotel.name}\n" \
			 f"🏢 Адрес отеля: {hotel.address}\n" \
			 f"🌐 Сайт: https://www.hotels.com/h{hotel.hotel_id}.Hotel-Information\n" \
			 f"🚍 Расстояние до центра: {round(hotel.distance, 1)} Км\n" \
			 f"💵 Стоимость проживания в сутки {round(hotel.price, 2)}\n" \

	if hotel.user_rates:
		string += f"⭐ рейтинг по мнению посетителей {hotel.user_rates}\n"

	return string