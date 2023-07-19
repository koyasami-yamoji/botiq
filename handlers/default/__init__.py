from aiogram import Router

from . import start, help


def handlers_default_command() -> Router:
    router = Router()

    router.include_router(start.router)
    router.include_router(help.router)
    return router
