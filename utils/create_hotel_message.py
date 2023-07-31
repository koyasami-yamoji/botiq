
from aiogram.types import Message, InputMediaPhoto
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from db.write_photo import set_record_photo


async def create_hotel_message(message: Message, hotel: dict, data: dict, session: AsyncSession):
	string = f"🏙 Название отеля: {hotel['name']}\n" \
			 f"🏢 Адрес отеля: {hotel['address']}\n" \
			 f"🌐 Сайт: https://www.hotels.com/h{hotel['id']}.Hotel-Information\n" \
			 f"🚍 Расстояние до центра: {round(hotel['distance'], 1)} Км\n" \
			 f"💵 Стоимость проживания в сутки {round(hotel['price'], 2)}\n" \

	if hotel.get('user_rating'):
		string += f"⭐ рейтинг по мнению посетителей {hotel['user_rating']}\n"

	image_url = [hotel['images'][url] for url in range(int(data['count_photo']))]
	medias = []

	if image_url:
		await set_record_photo(images=image_url, hotel_id=int(hotel['id']), session=session)
		medias.append(InputMediaPhoto(media=image_url[0], caption=string))
		for index, url in enumerate(image_url[1:]):
			medias.append(InputMediaPhoto(media=url))

		# await message.answer(text=string)
		await message.answer_media_group(media=medias)
	else:
		await message.answer(text=string)

	logger.info(f'Вывод в чат информацию о отеле. User_id {message.chat.id}')