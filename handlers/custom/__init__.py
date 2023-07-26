from aiogram import Router

from . import get_command, get_city, get_count_hotels, get_count_photo, get_price_hotel, get_distance_to_center


def setup_custom_handlers():
    router = Router()
    router.include_router(get_command.router)
    router.include_router(get_city.router)
    router.include_router(get_count_hotels.router)
    router.include_router(get_count_photo.router)
    router.include_router(get_price_hotel.router)
    router.include_router(get_distance_to_center.router)
    return router
