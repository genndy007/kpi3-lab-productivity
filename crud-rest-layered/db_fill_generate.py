import random
import string
from database import DB


def rnd_str():
    return ''.join(random.choices(string.ascii_uppercase, k=10))


def generate_data_in_db(amt: int):
    # apartment_id |   city   |    street     | house_num | floor_num | room_amt | square_amt |  cost
    db = DB.Instance()

    with db.conn as conn:
        with conn.cursor() as cur:
            for i in range(amt):
                city = rnd_str()
                street = rnd_str()
                house_num = random.randint(1, 100)
                floor_num = random.randint(1, 10)
                room_amt = random.randint(1, 6)
                square_amt = random.randint(30, 200)
                cost = random.randint(100000, 500000)

                sql = f'''insert into apartment(city, street, house_num, floor_num, room_amt, square_amt, cost)
                values ('{city}', '{street}', {house_num}, {floor_num}, {room_amt}, {square_amt}, {cost})'''
                cur.execute(sql)

        conn.commit()


if __name__ == "__main__":
    generate_data_in_db(100000)
