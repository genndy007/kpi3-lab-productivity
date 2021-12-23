from flask import Flask, request
from request_handling import GETHandler, POSTHandler, PATCHHandler, DELETEHandler



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def application():

    getHandler = GETHandler()
    postHandler = POSTHandler()
    patchHandler = PATCHHandler()
    deleteHandler = DELETEHandler()

    getHandler.set_next(postHandler).set_next(
        patchHandler).set_next(deleteHandler)

    return getHandler.handle(request)


if __name__ == "__main__":
    app.run(debug=True)
