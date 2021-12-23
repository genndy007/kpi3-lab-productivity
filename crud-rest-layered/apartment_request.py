# builder
class ApartmentRequest:
    def __init__(self, table_name):
        self.__request = f'select * from {table_name}'
        self.__conditions = []

    def add_condition_city(self, city):
        cond = f"city='{city}'"
        self.__conditions.append(cond)

    def add_condition_floor_num(self, floor_num):
        cond = f'floor_num={floor_num}'
        self.__conditions.append(cond)

    def add_condition_room_amt(self, room_amt):
        cond = f'room_amt={room_amt}'
        self.__conditions.append(cond)

    def add_condition_min_square_amt(self, min_square_amt):
        cond = f'square_amt>={min_square_amt}'
        self.__conditions.append(cond)

    def add_condition_max_square_amt(self, max_square_amt):
        cond = f'square_amt<={max_square_amt}'
        self.__conditions.append(cond)

    def add_condition_min_cost(self, min_cost):
        cond = f'cost>={min_cost}'
        self.__conditions.append(cond)

    def add_condition_max_cost(self, max_cost):
        cond = f'cost<={max_cost}'
        self.__conditions.append(cond)

    def get_request(self):
        return self.__request

    def create_request(self):
        if not self.__conditions:
            return

        self.__request += ' where '
        cond = ' and '.join(self.__conditions)
        self.__request += cond
