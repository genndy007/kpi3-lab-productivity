from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from db.orm.tables import Apartment

db_string = "postgresql://postgres:postgres@localhost:5432/search_query"

engine = create_engine(db_string)
db = scoped_session(sessionmaker(bind=engine))

# result = db.execute('select * from apartment')
# for r in result:
#     print(r)

result = db.query(Apartment).filter()


def get_apartment_by_params(params: dict):
    city = params.get('city')
    street = params.get('street')
    floor_num = params.get('floor_num')
    room_amt = params.get('room_amt')
    min_square_amt = params.get('min_square_amt')
    max_square_amt = params.get('max_square_amt')
    min_cost = params.get('min_cost')
    max_cost = params.get('max_cost')

    result = db.query(Apartment).filter(Apartment.city == city).all()
    print(result)
    return result
