import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

API_URL = 'https://swapi.dev/api/people/'

# подключение к БД
PG_DSN = f"postgres://castom:castom@127.0.0.1:5432/advertisement"
db_engine = create_engine(PG_DSN)
db_session = sessionmaker(bind=db_engine)


# получаем синхроно общее число героев вселенной
def heroesCount():
    count = requests.get(API_URL).json()
    return count["count"] + 1


MAX = heroesCount()
ALL_IDS = range(1, MAX + 1)
PARTITION = 10

