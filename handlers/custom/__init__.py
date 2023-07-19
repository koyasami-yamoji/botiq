from aiogram import Router

from . import input_data


def custom_handlers_routers():
    router = Router()
    router.include_router(input_data.router)
    return router
