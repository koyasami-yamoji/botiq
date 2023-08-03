from aiogram.types import Message
from loguru import logger

from keyboards.inline.calendar.calendar import Calendar


bot_calendar = Calendar()


async def my_calendar(message: Message, word: str):
    """
    Создание календаря и вывод его в бота
    :param message: Message
    :param word: str заезда/выезда
    :return: None
    """
    logger.info(f'Вызов календаря {word} User_id {message.chat.id}')
    await message.answer(f'Выберете дату {word}', reply_markup=bot_calendar.create_calendar())
