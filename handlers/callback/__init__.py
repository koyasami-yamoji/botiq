from aiogram import Router

from . import need_photo
from . import choice_city
from . import select_date


def setup_callback_handlers():
	router = Router()
	router.include_router(need_photo.router)
	router.include_router(choice_city.router)
	router.include_router(select_date.router)
	return router