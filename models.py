import datetime
from sqlalchemy import Column, Integer, String, Float, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# Create models here
class GeminiPrice(Base):
    __tablename__ = 'gemini_price'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ticker = Column(String)
    observation_time = Column(DateTime)
    last = Column(Float)
    bid = Column(Float)
    ask = Column(Float)
    volume = Column(Float)
    las_update = Column(DateTime, default=datetime.datetime.utcnow())
