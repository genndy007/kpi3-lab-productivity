# facade
import datetime
from apartment_request import ApartmentRequest
from filtering import City, FloorNum, RoomAmt, MinSquareAmt, MaxSquareAmt, MinCost, MaxCost
from database import DB
from apis.detail.get_apartments import DetailAPI
from apis.search.get_apartments import SearchAPI
from caching import Cache
import time

table_name = 'apartment'

cache = Cache()


class ApartmentFacade:
    def __init__(self) -> None:
        self.db = DB.Instance()
        self.time_of_update = None

    def __get_from_native_db(self, args):
        db_request = ApartmentRequest(table_name)
        if city := args.get('city'):
            db_request.add_condition_city(city)
        if floor_num := args.get('floor_num'):
            db_request.add_condition_floor_num(floor_num)
        if room_amt := args.get('room_amt'):
            db_request.add_condition_room_amt(room_amt)
        if min_square_amt := args.get('min_square_amt'):
            db_request.add_condition_min_square_amt(min_square_amt)
        if max_square_amt := args.get('max_square_amt'):
            db_request.add_condition_max_square_amt(max_square_amt)
        if min_cost := args.get('min_cost'):
            db_request.add_condition_min_cost(min_cost)
        if max_cost := args.get('max_cost'):
            db_request.add_condition_max_cost(max_cost)

        db_request.create_request()
        sql = db_request.get_request()

        with self.db.conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()

        return [list(row) for row in rows]

    def __get_from_detail(self, args: dict):
        detail = DetailAPI()
        all_apas = detail.get_all_apartments_by_page()

        spec = True
        if city := args.get('city'):
            spec = spec and City(city)
        if floor_num := args.get('floor_num'):
            spec = spec and FloorNum(floor_num)
        if room_amt := args.get('room_amt'):
            spec = spec and RoomAmt(room_amt)
        if min_square_amt := args.get('min_square_amt'):
            spec = spec and MinSquareAmt(min_square_amt)
        if max_square_amt := args.get('max_square_amt'):
            spec = spec and MaxSquareAmt(max_square_amt)
        if min_cost := args.get('min_cost'):
            spec = spec and MinCost(min_cost)
        if max_cost := args.get('max_cost'):
            spec = spec and MaxCost(max_cost)

        filtered_apas = []
        for apa in all_apas:
            if spec.is_satisfied_by(apa):
                filtered_apas.append(apa)

        return filtered_apas

    def __get_from_search(self, args):
        search = SearchAPI()
        apas = search.get_apartments_by_params(args)
        return apas

    def get_apartments(self, request):
        if not self.time_of_update or (datetime.datetime.now() - self.time_of_update).days == 1:
            cache.clear()

        args = request.args

        all_results = []

        rows_native_db = self.__get_from_native_db(args)

        if cache.is_empty():
            self.time_of_update = datetime.datetime.now()
            rows_detail = self.__get_from_detail(args)
            rows_search = self.__get_from_search(args)

            for row in rows_detail:
                cache.add(row)
            for row in rows_search:
                cache.add(row)

        for row in rows_native_db:
            all_results.append(row)
        for row in cache.cache:
            all_results.append(row)

        return all_results

    def add_apartment(self, request):
        apa = request.json

        city = apa['city']
        street = apa['street']
        house_num = apa['house_num']
        floor_num = apa['floor_num']
        room_amt = apa['room_amt']
        square_amt = apa['square_amt']
        cost = apa['cost']

        sql = f'''INSERT INTO {table_name}(city, street, house_num, floor_num, room_amt, square_amt, cost) 
        VALUES ('{city}', '{street}', {house_num}, {floor_num}, {room_amt}, {square_amt}, {cost})
        RETURNING apartment_id
        '''

        id_of_new_row = None
        with self.db.conn.cursor() as cur:
            cur.execute(sql)
            id_of_new_row = cur.fetchone()[0]

        self.db.conn.commit()

        return id_of_new_row

    def update_apartment(self, request):
        apa = request.json

        apartment_id = apa['apartment_id']
        city = apa['city']
        street = apa['street']
        house_num = apa['house_num']
        floor_num = apa['floor_num']
        room_amt = apa['room_amt']
        square_amt = apa['square_amt']
        cost = apa['cost']

        sql = f'''UPDATE {table_name}
        SET city = '{city}',
            street = '{street}',
            house_num = {house_num},
            floor_num = {floor_num},
            room_amt = {room_amt},
            square_amt = {square_amt},
            cost = {cost} 
        WHERE apartment_id = {apartment_id}
        RETURNING apartment_id
        '''

        id_of_new_row = None
        with self.db.conn.cursor() as cur:
            cur.execute(sql)
            id_of_new_row = cur.fetchone()[0]

        self.db.conn.commit()

        return id_of_new_row

    def remove_apartment(self, request):
        apa = request.json

        apartment_id = apa['apartment_id']

        sql = f'''DELETE FROM {table_name}
        WHERE apartment_id = {apartment_id}
        RETURNING apartment_id
        '''

        id_of_new_row = None
        with self.db.conn.cursor() as cur:
            cur.execute(sql)
            id_of_new_row = cur.fetchone()[0]

        self.db.conn.commit()

        return id_of_new_row


if __name__ == '__main__':
    facade = ApartmentFacade()
    res = facade.get_apartments({'room_amt': 3})
    print(res[-1])
