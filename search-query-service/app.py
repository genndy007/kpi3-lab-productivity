from flask import Flask
from flask import request
import time
import random

from connect_db import get_apartments_from_db

app = Flask(__name__)


@app.route('/')
def main():
    return 'hello world'


MIN_RESP_TIME = 0
MAX_RESP_TIME = 0


@app.route('/search')
def search():
    time.sleep(random.randint(MIN_RESP_TIME, MAX_RESP_TIME))
    apartments = get_apartments_from_db(request.args)
    print(apartments)
    return {'apartments': apartments}


if __name__ == '__main__':
    app.run(port=5001, debug=True)
