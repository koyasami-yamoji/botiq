from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from config_data.config import DEFAULT_COMMANDS


router = Router()


@router.message(Command('help'))
async def bot_help(message: Message) -> None:
    await message.answer('/n'.join([f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]))
