import asyncio
import json
from utils.parse_result import parse_result
from aiogram.types import Message
from api.api_request import api_request
from api.request_photo_and_hotel_info import request_photo_and_hotel_info
from utils.create_hotel_message import create_hotel_message
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from db.write_hotels import set_record_hotels
from db.write_history import set_record_history


async def find_hotel(message: Message, data: dict, state: FSMContext, session: AsyncSession) -> None:
    """
    Формирования запроса об отеле и отправка запроса.
    Вывод полученной информации пользователю
    :param session: AsyncSession
    :param state: FSMContext
    :param message: Message
    :param data: Dict Данные собранные от пользователя
    :return: None
    """
    if data['command'] == '/lower':
        result_size = int(data['count_hotels'])
    else:
        result_size = 200

    if data['command'] == '/custom':
        min_price = int(data['min_price'])
        max_price = int(data['max_price'])
    else:
        min_price = ""
        max_price = ""

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "destination": {
            "regionId": data['destination_id']
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
        "resultsSize": result_size,
        "sort": data['sort'],
        "filters": {
            "price": {
                "max": max_price,
                "min": min_price
            }
        }
    }
    url = "https://hotels4.p.rapidapi.com/properties/v2/list"
    payload = json.dumps(payload)
    await message.answer('Ищем отели...Подождите')
    bot = message.get_mounted_bot()
    await bot.send_chat_action(chat_id=message.chat.id, action="typing", request_timeout=10)
    response_hotel = await api_request(message, method_type='POST', url=url, data=payload)
    data_request = json.loads(response_hotel)

    record_history = await set_record_history(data, session)
    if not data_request:
        raise LookupError('Упс...Запрос пуст..')
    parsed_hotels = parse_result(message, parse_list=data_request['data']['propertySearch']['properties'], data=data)
    if 'error' in parsed_hotels:
        await message.answer(f'{parsed_hotels["error"]}\n Ошибка, попробуйте ввести другие параметры')
    if parsed_hotels:
        count = 0
        for hotel in parsed_hotels.values():
            if count < int(data['count_hotels']):
                count += 1
                info = await request_photo_and_hotel_info(message, hotel['id'])
                hotel['address'] = info['address']
                parsed_hotels[hotel['address']] = info['address']
                hotel['images'] = info['images']

                await create_hotel_message(message=message, hotel=hotel, data=data, session=session)
        await set_record_hotels(hotels=parsed_hotels, record_history=record_history, session=session)
    await session.close()
    await message.answer('Поиск закончен')
    await state.set_state(None)