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


def parse_url_args(params: dict):
    sql = 'select * from apartment '
    if params:
        sql += 'where '

    for k, v in params.items():
        if 'min' in k:
            name = k.lstrip('min_')
            sql += f"{name}>{v} and "
            continue
        if 'max' in k:
            name = k.lstrip('max_')
            sql += f"{name}<{v} and "
            continue

        sql += f"{k}='{v}' and "

    sql = sql.rstrip('and ')

    return sql


def get_apartments_from_db(args: dict):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        sql = parse_url_args(args)
        cur.execute(sql)

        # display the PostgreSQL database server version
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
