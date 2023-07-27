import os
from dotenv import find_dotenv, load_dotenv
from aiogram.types.bot_command import BotCommand


if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

    bot_token = os.getenv('BOT_TOKEN')
    rapid_api_token = os.getenv("rapid_api_key")
    host = os.getenv('HOST')
    port = os.getenv("PORT")
    user_name = os.getenv('USER_NAME')
    password = os.getenv('PASSWORD')
    db_name = os.getenv('DATABASE')

DEFAULT_COMMANDS = [
    BotCommand(command="start", description="Запустить бота"),
    BotCommand(command="help", description="Вывести справку"),
    BotCommand(command="lower", description="Вывод самых дешевых отелей в городе"),
    BotCommand(command="higher", description="Вывод самых дорогих отелей в городе"),
    BotCommand(command="custom", description="Расширенный поиск."),
    BotCommand(command="history", description="Показать историю поиска"),
]