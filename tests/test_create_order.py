import json
import allure
import pytest
import requests
from data import Order
from url import Url
from endpoints import Endpoints


class TestCreateOrder:
    path = f"{Url.URL_SERVICE}{Endpoints.CREATE_ORDER}"
    payload_order = None

    @classmethod
    def setup_class(cls):
        cls.payload_order = Order.payload_order
        return cls.payload_order

    @allure.title('Заказ можно создать с любым цветом самоката')
    @allure.step(f'Отправить POST запрос на эндпоинт {Endpoints.CREATE_ORDER} с выбранным цветом самоката')
    @pytest.mark.parametrize(
        'color', [
            pytest.param(([]), id="color: []"),
            pytest.param((["BLACK"]), id='color: ["BLACK"]'),
            pytest.param((["GREY"]), id='color: ["GREY"]'),
            pytest.param((["BLACK", "GREY"]), id='color: ["BLACK", "GREY"]')
        ])
    def test_create_order_with_color_scooter(self, color):
        self.payload_order["color"] = color
        p_string = json.dumps(self.payload_order)
        headers = {"Content-type": "application/json"}
        response = requests.post(self.path, data=p_string, headers=headers)
        assert response.status_code == 201

    @allure.title('Успешный запрос на созданние заказа возвращает track-номер заказа')
    @allure.step(f'Отправить POST запрос на эндпоинт {Endpoints.CREATE_ORDER} для создания заказа')
    def test_create_order_return_correct_text(self):
        p_string = json.dumps(self.payload_order)
        headers = {"Content-type": "application/json"}
        response = requests.post(self.path, data=p_string, headers=headers)
        assert "track" in response.text

    @classmethod
    def teardown_class(cls):
        cls.payload_order.clear()
