# Stock Data from Polygon.io API

This is a web API application that retrieves stock data from an external financial API and performs small data scrapings
from the financial website Marketwatch.

### Raw project initialization (without Docker environment)
```
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### Create .env File (needs to be into Root project folder):
| Parameter     | Descrição                                       |
|:--------------|:------------------------------------------------|
| `user`        | Your Postgres Installation user                 |
| :----------   | :------------------------------------           |
| `password`    | Your Postgres Installation password             |
| :------------ | :--------------------------------------         |
| `port`        | Your Postgres Installation Port (commonly 5432) |
| :------------ | :--------------------------------------         |
| `db_name`     | **Mandatory**: stockdb                          |
| :------------ | :--------------------------------------         |
```
DATABASE_URL=postgresql://<user>:<password>@localhost:<port>/<db_name>
POLYGON_API_KEY=bmN7i7CrzrpKqFvgbB1fEaztCwZKSUjJ
```
stockdb
### Script to create PostgreSQL Database:
```
Minumum version: PostgreSQL 16
initdb.sql
```

### Start the FastAPI uvicorn server:
```
uvicorn app.main:app --reload
```
### API Access:
```
http://127.0.0.1:8000/docs
```

# Running project with Docker Environment: