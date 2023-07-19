from aiogram import Router

from .custom import custom_handlers_routers
from .default import handlers_default_command


def get_handlers_router() -> Router:
    router = Router()

    custom_router = custom_handlers_routers()
    default_router = handlers_default_command()

    router.include_router(custom_router)
    router.include_router(default_router)
    return router