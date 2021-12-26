from configparser import ConfigParser
import psycopg2
import string
import random


def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} not found in the {1} file'.format(section, filename))

    return db


def get_price_list_from_db(page: int):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        sql = f'select * from apartment limit 5000 offset {5000*(page-1)}'
        cur.execute(sql)

        apartments = cur.fetchall()

        # close the communication with the PostgreSQL
        cur.close()

        return apartments
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def get_details_by_id_from_db(id):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        sql = f'select * from apartment where apartment_id={id}'
        cur.execute(sql)

        apartment = cur.fetchone()
        print(apartment)

        # close the communication with the PostgreSQL
        cur.close()

        return apartment
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def rnd_str():
    return ''.join(random.choices(string.ascii_uppercase, k=10))


def generate_data_in_db(amt: int):
    # apartment_id |   city   |    street     | house_num | floor_num | room_amt | square_amt |  cost
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

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

        # close the communication with the PostgreSQL
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == "__main__":
    generate_data_in_db(50000)
