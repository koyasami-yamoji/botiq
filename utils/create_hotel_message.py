
from aiogram.types import Message, InputMediaPhoto
from loguru import logger
from db.write_photo import set_photo
from sqlalchemy.orm import Session


async def create_hotel_message(message: Message, hotel: dict, data: dict, session: Session):
	string = f"🏙 Название отеля: {hotel['name']}\n" \
			 f"🏢 Адрес отеля: {hotel['address']}\n" \
			 f"🌐 Сайт: f'https://www.hotels.com/h{hotel['id']}.Hotel-Information\n" \
			 f"🚍 Расстояние до центра: {hotel['distance']} Км\n" \
			 f"💵 Стоимость проживания в сутки {hotel['price']}\n" \
			 f"⭐ рейтинг по мнению посетителей {hotel['user_rating']}\n" \

	image_url = [hotel['images'][url] for url in range(int(data['count_photo']))]
	medias = []
	if image_url:
		for index, url in enumerate(image_url):
			set_photo(photo=hotel['images'], session=session)
			medias.append(InputMediaPhoto(media=url))

		await message.answer(text=string)
		await message.answer_media_group(media=medias, reply_to_message_id=message.message_id)
	else:
		await message.answer(text=string)

	logger.info(f'Вывод в чат информацию о отеле. User_id {message.chat.id}')