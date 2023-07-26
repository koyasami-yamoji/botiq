from aiogram import Router

from .custom import setup_custom_handlers
from .default import setup_default_handlers
from .callback import setup_callback_handlers


def get_handlers_router() -> Router:
    router = Router()

    custom_router = setup_custom_handlers()
    default_router = setup_default_handlers()
    callback_router = setup_callback_handlers()

    router.include_router(custom_router)
    router.include_router(default_router)
    router.include_router(callback_router)

    return router