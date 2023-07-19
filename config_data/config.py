import os
from dotenv import find_dotenv, load_dotenv


if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("lower", "Вывод самых дешевых отелей в городе"),
    ("high", "Вывод самых дорогих отелей в городе"),
    ("custom", "Кастом."),
    ("history", "Показать историю поиска"),
)