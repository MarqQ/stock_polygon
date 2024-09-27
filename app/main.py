from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine
import requests
import os
from dotenv import load_dotenv

# Buscando as variáveis do arquivo .env
load_dotenv()

app = FastAPI()

# Criação das tabelas no Postgre
models.Base.metadata.create_all(bind=engine)


# Retorno da sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoint para aquisição dos dados (GET)
@app.get("/v1/open-close/{stocksTicker}/{date}", response_model=schemas.Stock)
def get_stock_data(stocksTicker: str, date: str, db: Session = Depends(get_db)):
    # Chamada à API externa da Polygon
    api_key = os.getenv("POLYGON_API_KEY")
    url = f"https://api.polygon.io/v1/open-close/{stocksTicker}/{date}?adjusted=true&apiKey={api_key}"
    headers = {"Authorization": f"Bearer {api_key}"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching stock data")

    data = response.json()

    # Dados da API para salvar no banco de dados
    # stock_data = crud.create_stock(db=db, stock_data=data)

    return data


# Endpoint para atualizar o valor adquirido da API externa (POST)
@app.post("/stock/{stock_symbol}")
def update_stock(stock_symbol: str, amount: schemas.Stock, db: Session = Depends(get_db)):
    stock = crud.get_stock_by_symbol(db, stock_symbol)

    if stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")

    stock = crud.update_stock_purchase(db=db, stock=stock, amount=amount.amount)

    return {"message": f"{amount.amount} units of stock {stock_symbol} added successfully."}
