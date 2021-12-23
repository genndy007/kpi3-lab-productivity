from flask import Flask
from flask import request

from connect_db import get_apartments_from_db

app = Flask(__name__)


@app.route('/')
def main():
    return 'hello world'


@app.route('/search')
def search():
    apartments = get_apartments_from_db(request.args)
    print(apartments)
    return {'apartments': apartments}


if __name__ == '__main__':
    app.run(port=5001, debug=True)
