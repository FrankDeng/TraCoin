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


# live data models
class CurrentPrice(ModelBase, Base):
    __tablename__ = 'current_prices'

    last = Column(Float)
    bid = Column(Float)
    ask = Column(Float)
    volume = Column(Float)


class OrderBook(ModelBase, Base):
    __tablename__ = 'order_book'

    side = Column(String)
    price = Column(Float)
    amount = Column(Float)


class RecentTrades(ModelBase, Base):
    __tablename__ = 'recent_trades'

    side = Column(String)
    price = Column(Float)
    amount = Column(Float)


# historical data models
class HistoricalPrices(ModelBase, Base):
    __tablename__ = 'historical_prices'

    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)
