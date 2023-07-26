import aiohttp
from aiogram.types import Message
from config_data import config
from loguru import logger


async def api_request(message: Message, method_type: str, url: str, params: dict = None, data: dict = None):
	"""
		Отправка запроса на сервер
		:param data:
		:param message:  Message
		:param method_type:  str
		:param url:  str
		:param params: dict
		:return: None
	"""
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": config.rapid_api_token,
		"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
	}
	if params:
		async with aiohttp.request(method=method_type, url=url, headers=headers, params=params) as response:
			if response.status == 200:
				logger.info(f'Сервер ответил. Статус запроса {response.status}')
				return await response.text()
			else:
				logger.error(f'Ошибка запроса. код ошибки {response.status}')
				await message.answer(f'Ошибка запроса. Код ошибки - {response.status}')
				await message.answer('Выполните команду еще раз')



