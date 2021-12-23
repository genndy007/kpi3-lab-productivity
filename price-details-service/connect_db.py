from configparser import ConfigParser
import psycopg2


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


def get_price_list_from_db():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        sql = 'select apartment_id, cost from apartment'
        cur.execute(sql)

        apartments = cur.fetchall()
        print(apartments)

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
