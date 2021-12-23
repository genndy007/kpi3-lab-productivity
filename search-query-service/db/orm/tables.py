from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.sqltypes import Numeric


Base = declarative_base()


class Apartment(Base):
    __tablename__ = 'apartment'

    apartment_id = Column(Integer, primary_key=True)
    city = Column(String)
    street = Column(String)
    house_num = Column(Integer)
    floor_num = Column(Integer)
    room_amt = Column(Integer)
    square_amt = Column(Numeric)
    cost = Column(Numeric)
