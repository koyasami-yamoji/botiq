from aiogram.fsm.state import StatesGroup, State


class HotelInfoState(StatesGroup):
    city = State()
    count_days = State()
    min_distance_to_center = State()
    max_distance_to_center = State()
    count_photo = State()
    date = State()
    max_price = State()
    min_price = State()
    count_hotels = State()
    out_date = State()
    select_number = State()
