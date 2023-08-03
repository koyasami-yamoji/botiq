from sqlalchemy import Integer, BigInteger, Date, DateTime, ForeignKey, String, Numeric
from sqlalchemy.orm import mapped_column

from db.base import Base


class History(Base):
    __tablename__ = 'history'

    id = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = mapped_column(BigInteger, nullable=False, index=True)
    date_time = mapped_column(DateTime, nullable=False)
    city = mapped_column(String, nullable=False)
    command = mapped_column(String, nullable=False)
    check_in = mapped_column(Date, nullable=False)
    check_out = mapped_column(Date, nullable=False)
    min_price = mapped_column(Integer, nullable=True)
    max_price = mapped_column(Integer, nullable=True)
    min_distance = mapped_column(Integer, nullable=True)
    max_distance = mapped_column(Integer, nullable=True)
    count_hotels = mapped_column(Integer, nullable=False)
    count_photo = mapped_column(Integer, nullable=False)
    destination_id = mapped_column(BigInteger, nullable=False)
    sort = mapped_column(String, nullable=False)


class Hotels(Base):
    __tablename__ = 'hotels'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    history_id = mapped_column(Integer, ForeignKey('history.id', ondelete='CASCADE'), nullable=False, index=True)
    hotel_id = mapped_column(BigInteger, nullable=False)
    name = mapped_column(String, nullable=False)
    address = mapped_column(String, nullable=False)
    price = mapped_column(Numeric, nullable=False)
    distance = mapped_column(Numeric, nullable=False)
    user_rates = mapped_column(Numeric, nullable=True)


class Photo(Base):
    __tablename__ = "photo"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    hotel_id = mapped_column(BigInteger, nullable=False, index=True)
    photo = mapped_column(String, nullable=False)