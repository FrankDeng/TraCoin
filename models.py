import datetime
from sqlalchemy import Column, Integer, String, Float, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# Create models here
class ModelBase(object):
    id = Column(Integer, primary_key=True, autoincrement=True)
    ticker = Column(String)
    utc_time = Column(DateTime)
    source = Column(String)
    last_update = Column(DateTime, default=datetime.datetime.utcnow)


# Gemini models
class GeminiPrice(ModelBase, Base):
    __tablename__ = 'gemini_price'

    last = Column(Float)
    bid = Column(Float)
    ask = Column(Float)
    volume = Column(Float)


class GeminiOrderBook(ModelBase, Base):
    __tablename__ = 'gemini_order_book'

    side = Column(String)
    price = Column(Float)
    amount = Column(Float)


class GeminiTrades(ModelBase, Base):
    __tablename__ = 'gemini_trades'

    side = Column(String)
    price = Column(Float)
    amount = Column(Float)
