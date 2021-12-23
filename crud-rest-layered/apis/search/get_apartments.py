import requests


class SearchAPI:
    PORT = 5001

    def get_apartments_by_params(self, params: dict):
        url = f'http://localhost:{self.PORT}/search'
        resp = requests.get(url, params)
        data = resp.json()

        return data['apartments']


if __name__ == "__main__":
    search = SearchAPI()
    print(search.get_apartments_by_params({}))
