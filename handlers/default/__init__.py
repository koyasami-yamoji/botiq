from aiogram import Router

from . import start, help


def setup_default_handlers() -> Router:
    router = Router()

    router.include_router(start.router)
    router.include_router(help.router)
    return router
