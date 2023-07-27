import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode
from config_data import config
from handlers import get_handlers_router
from loguru import logger


async def main():
    logger.add("debug.log", format="{time} {level} {message}", level='DEBUG')
    bot = Bot(token=config.bot_token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(get_handlers_router())
    await bot.set_my_commands(commands=config.DEFAULT_COMMANDS)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        logger.info('Начало работы.')
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info('Остановка работы.')
