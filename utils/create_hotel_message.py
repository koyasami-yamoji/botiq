
from aiogram.types import Message, InputMediaPhoto
from loguru import logger


async def create_hotel_message(message: Message, hotel: dict, data: dict):
	string = f"🏙 Название отеля: {hotel['name']}\n" \
			 f"🏢 Адрес отеля: {hotel['address']}\n" \
			 f"🌐 Сайт: https://www.hotels.com/ho{hotel['id']}\n" \
			 f"🚍 Расстояние до центра: {hotel['distance']} Км\n" \
			 f"💵 Стоимость проживания в сутки {hotel['price']}\n" \
			 f"⭐ рейтинг по мнению посетителей {hotel['user_rating']}\n" \
			 f"🗺 Отель на карте: https://maps.google.com/maps?z=12&t=m&q=loc:{hotel['coordinates']}"

	image_url = [hotel['images'][url] for url in range(int(data['count_photo']))]
	medias = []
	if image_url:
		for index, url in enumerate(image_url):
			medias.append(InputMediaPhoto(media=url))

		await message.answer(text=string)
		await message.answer_media_group(media=medias)
	else:
		await message.answer(text=string)

	logger.info(f'Вывод в чат информацию о отеле. User_id {message.message.chat.id}')