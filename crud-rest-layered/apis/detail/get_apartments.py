import requests


class DetailAPI:
    PORT = 5002

    def get_all_apartments(self):
        url = f'http://localhost:{self.PORT}/price-list'
        resp = requests.get(url)
        data = resp.json()
        return data['price_list']

    def get_one_apartment_details(self, id):
        url = f'http://localhost:{self.PORT}/details/{id}'
        resp = requests.get(url)
        data = resp.json()
        return data['details']

    def get_ids_by_cost(self, data: list[list[int, int]], min_cost=-float('inf'), max_cost=float('inf')):
        ids_list = []
        for apa in data:
            apa_id, cost = apa
            if min_cost < cost < max_cost:
                ids_list.append(apa_id)

        return ids_list

    def get_apartments_details(self, ids: list[int]):
        details = []
        for i in ids:
            detail = self.get_one_apartment_details(i)
            details.append(detail)

        return details

    def get_apartments_by_params(self, min_cost=-float('inf'), max_cost=float('inf')):
        # 1. take all apa
        apa = self.get_all_apartments()
        # 2. filter ids by cost
        ids = self.get_ids_by_cost(apa, min_cost=min_cost, max_cost=max_cost)
        # 3. get other info by id
        apa_details = self.get_apartments_details(ids)
        return apa_details


if __name__ == "__main__":
    detail = DetailAPI()
    print(detail.get_apartments_by_params())
