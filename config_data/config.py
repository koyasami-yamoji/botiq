import os
from dotenv import find_dotenv, load_dotenv


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

DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("lower", "Вывод самых дешевых отелей в городе"),
    ("high", "Вывод самых дорогих отелей в городе"),
    ("custom", "Расширенный поиск."),
    ("history", "Показать историю поиска"),
)