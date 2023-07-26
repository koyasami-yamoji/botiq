import json
from utils.parse_result import parse_result
from aiogram.types import Message
from api.api_request import api_request
from api.request_photo import request_photo
from utils.create_hotel_message import create_hotel_message
from aiogram.fsm.context import FSMContext


async def find_hotel(message: Message, data: dict, state: FSMContext = None) -> None:
	"""
	Формирования запроса об отеле и отправка запроса.
	Вывод полученной информации пользователю
	:param state: FSMContext
	:param message: Message
	:param data: Dict Данные собранные от пользователя
	:return: None
	"""
	if data['command'] == '/custom':
		min_price = int(data['min_price'])
		max_price = int(data['max_price'])
	else:
		min_price = ''
		max_price = ''

	payload = {
		"currency": "USD",
		"eapid": 1,
		"locale": "en_US",
		"siteId": 300000001,
		"destination": {
			"regionId": int(data['destination_id'])
		},
		"checkInDate": {
			"day": int(data['CheckInDate']['day']),
			"month": int(data['CheckInDate']['month']),
			"year": int(data['CheckInDate']['year'])
		},
		"checkOutDate": {
			"day": int(data['CheckOutDate']['day']),
			"month": int(data['CheckOutDate']['month']),
			"year": int(data['CheckOutDate']['year'])
		},
		"rooms": [
			{
				"adults": 2,
				"children": [{"age": 5}, {"age": 7}]
			}
		],
		"resultsStartingIndex": 0,
		"resultsSize": 200,
		"sort": data['sort'],
		"filters": {
			"price": {
				"max": max_price,
				"min": min_price
			}
		}
	}
	url = "https://hotels4.p.rapidapi.com/properties/v2/list"
	response_hotel = await api_request(message, method_type='POST', url=url, data=payload)
	data_request = json.loads(response_hotel)
	if not data_request:
		raise LookupError('Упс...Запрос пуст..')
	parsed_hotels = parse_result(parse_list=data_request['data']['propertySearch']['properties'], data=data)
	if 'error' in parsed_hotels:
		await message.answer(f'{parsed_hotels["error"]}\n Ошибка, попробуйте ввести другие параметры')
	if parsed_hotels:
		for count, hotel in enumerate(parsed_hotels):
			if count + 1 < data['count_hotels']:
				info = await request_photo(message, hotel['id'])
				hotel['address'] = info['address']
				hotel['coordinates'] = info['coordinates']
				hotel['images'] = info['images']
				await create_hotel_message(message=message, hotel=hotel, data=data)

	await message.answer('Поиск закончен')
	await state.set_state(None)