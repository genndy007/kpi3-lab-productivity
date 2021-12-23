from flask import Flask
from flask import request

from connect_db import get_price_list_from_db, get_details_by_id_from_db

app = Flask(__name__)


@app.route('/')
def main():
    return 'hello world'


@app.route('/price-list')
def all_apartments():
    apartments = get_price_list_from_db()
    return {'price_list': apartments}


@app.route('/details/<id>')
def apartment_details(id):
    apartment = get_details_by_id_from_db(id)
    return {'details': apartment}


if __name__ == '__main__':
    app.run(port=5002, debug=True)
