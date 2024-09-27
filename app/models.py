from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base


class StockModel(Base):
    __tablename__ = 'stock_model'

    id = Column(Integer, primary_key=True, index=True)
    after_hours = Column(Float)
    close = Column(Float)
    from_date = Column(String)  # Usamos String pois o formato vem como string no JSON
    high = Column(Float)
    low = Column(Float)
    open = Column(Float)
    pre_market = Column(Float)
    status = Column(String)
    symbol = Column(String)
    volume = Column(Integer)
