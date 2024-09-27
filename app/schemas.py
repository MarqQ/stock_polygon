from pydantic import BaseModel


class Stock(BaseModel):
    after_hours: float
    close: float
    from_date: str
    high: float
    low: float
    open: float
    pre_market: float
    status: str
    symbol: str
    volume: int

    class Config:
        orm_mode = True
