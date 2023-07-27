from sqlalchemy import Column, Integer, BigInteger, Date, DateTime, Boolean, ForeignKey, String, Numeric
from db.base import Base


class History(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False, index=True)
    date_time = Column(DateTime, nullable=False)
    city = Column(String, nullable=False)
    command = Column(String, nullable=False)
    check_in_year = Column(Date, nullable=False)
    check_in_month = Column(Date, nullable=False)
    check_in_day = Column(Date, nullable=False)
    check_out_year = Column(Date, nullable=False)
    check_out_month = Column(Date, nullable=False)
    check_out_day = Column(Date, nullable=False)
    min_price = Column(Integer, nullable=True)
    max_price = Column(Integer, nullable=True)
    min_distance = Column(Integer, nullable=True)
    max_distance = Column(Integer, nullable=True)
    count_hotels = Column(Integer, nullable=False)
    count_photo = Column(Integer, nullable=False)
    destination_id = Column(BigInteger, nullable=False)
    sort = Column(String, nullable=False)


class Hotels(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True, autoincrement=True)
    history_id = Column(Integer, ForeignKey('history.id', ondelete='CASCADE'), nullable=False, index=True)
    hotel_id = Column(BigInteger, nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    price = Column(Numeric, nullable=False)
    distance = Column(Numeric, nullable=False)
    user_rates = Column(Numeric, nullable=True)
    images = Column(String, nullable=True)


class Photo(Base):
    __tablename__ = "photo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_id = Column(BigInteger, nullable=False, index=True)
    photo = Column(String, nullable=False)