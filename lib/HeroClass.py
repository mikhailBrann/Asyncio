from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Hero(Base):
    '''Класс персонажа из вселенной Star Wars'''

    __tablename__ = 'heroes'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=True, default='None')
    height = Column(String, nullable=True, default='None')
    mass = Column(String, nullable=True, default='None')
    hair_color = Column(String(80), nullable=True, default='None')
    skin_color = Column(String(120), nullable=True, default='None')
    eye_color = Column(String(80), nullable=True, default='None')
    birth_year = Column(String(120), nullable=True, default='None')
    gender = Column(String(80), nullable=True, default='None')
    homeworld = Column(String(120), nullable=True, default='None')
    films = Column(String, nullable=True, default='None')
    species = Column(String, nullable=True, default='None')
    vehicles = Column(String, nullable=True, default='None')
    starships = Column(String, nullable=True, default='None')

