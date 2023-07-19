from aiogram import Bot, Router
from aiogram.types import Message
from aiogram.filters import CommandStart


router = Router()


@router.message(CommandStart())
async def bot_start(message: Message, bot: Bot) -> None:
    bot_information = await bot.get_me()
    await message.reply(f'Привет <b>{message.from_user.full_name}</b> в <b>{bot_information.full_name}</b>\n'
                        f'<b>Для получения всех комманд и информации о них введите</b> /help')
