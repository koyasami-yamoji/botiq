from api.api_request import api_request
from aiogram.types import Message
import json


async def request_photo(message: Message, hotel_id: int):
	payload = {
		"currency": "USD",
		"eapid": 1,
		"locale": "en_US",
		"siteId": 300000001,
		"propertyId": hotel_id
	}
	summary_url = "https://hotels4.p.rapidapi.com/properties/v2/get-summary"
	summary_response = await api_request(message=message, method_type="POST", url=summary_url, params=payload)
	data = json.loads(summary_response)
	if not data:
		raise LookupError('Запрос пуст')
	info = {
		'address': data['data']['propertyInfo']['summary']['location']['address']['addressLine'],
		'coordinates': data['data']['propertyInfo']['summary']['location']['coordinates'],
		'images': [url['image']['url'] for url in data['data']['propertyInfo']['propertyGallery']['images']]
	}
	return info