import allure
import requests
import source
from url import Url
from endpoints import Endpoints


class TestListOrders:
    path = f"{Url.URL_SERVICE}{Endpoints.CREATE_ORDER}"

    @allure.title('Получение списка заказов курьера с лимитом 2шт')
    @allure.step(f'Отправить GET запрос на эндпоинт {Endpoints.CREATE_ORDER} с параметрами: courierId и limit')
    def test_order_list_with_courier_id_and_limit(self, create_new_courier):
        courier_id = source.get_id_courier(create_new_courier[0], create_new_courier[1])
        params = {"courierId": courier_id, "limit": 2}
        response = requests.get(self.path, params=params).json()
        assert response["orders"] == [] and response["pageInfo"]["limit"] == 2

    @allure.title('Получение списка заказов рядом со станцией метро "Бульвар Рокоссовского"')
    @allure.step(f'Отправить GET запрос на эндпоинт {Endpoints.CREATE_ORDER} с параметрами: nearestStation')
    def test_order_list_with_near_station(self):
        params = {"nearestStation": '["1"]'}
        response = requests.get(self.path, params=params).json()
        assert response["availableStations"][0]["name"] == "Бульвар Рокоссовского"
