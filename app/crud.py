from sqlalchemy.orm import Session
from app import models, schemas


def create_stock(db: Session, stock_data: dict):
    stock = models.StockModel(
        after_hours=stock_data.get('afterHours'),
        close=stock_data.get('close'),
        from_date=stock_data.get('from'),
        high=stock_data.get('high'),
        low=stock_data.get('low'),
        open=stock_data.get('open'),
        pre_market=stock_data.get('preMarket'),
        status=stock_data.get('status'),
        symbol=stock_data.get('symbol'),
        volume=stock_data.get('volume')
    )
    db.add(stock)
    db.commit()
    db.refresh(stock)
    return stock


def get_stock_by_symbol(db: Session, stock_symbol: str):
    return db.query(models.StockModel).filter(models.StockModel.company_code == stock_symbol).first()


def update_stock_purchase(db: Session, stock: models.StockModel, amount: int):
    stock.purchased_amount += amount
    db.commit()
    db.refresh(stock)
    return stock
