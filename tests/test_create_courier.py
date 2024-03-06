import allure
import pytest as pytest
import requests
from data import Courier
from url import Url
from endpoints import Endpoints


class TestCreateCourier:
    path = f"{Url.URL_SERVICE}{Endpoints.CREATE_COURIER}"

    @allure.title('Код ответа успешного запроса - 201')
    @allure.step(f'Отправить POST запрос на эндпоинт {Endpoints.CREATE_COURIER} для создания курьера')
    def test_create_courier_return_code_201(self, payload_create_courier):
        response = requests.post(self.path, data=payload_create_courier)
        assert response.status_code == 201

    @allure.title('Успешный запрос возвращает верный текст ответа')
    @allure.step(f'Отправить POST запрос на эндпоинт {Endpoints.CREATE_COURIER} для создания курьера')
    def test_create_courier_correct_response_text(self, payload_create_courier):
        response = requests.post(self.path, data=payload_create_courier)
        assert response.text == '{"ok":true}'

    @allure.title('Запрос на создание курьера с существующим логином возвращает ошибку')
    @allure.step(f'Отправить POST запрос на эндпоинт {Endpoints.CREATE_COURIER} с существующим логином')
    def test_create_courier_with_exist_login(self, create_new_courier, payload_create_courier):
        login = create_new_courier[0]
        password = payload_create_courier["password"]
        first_name = payload_create_courier["firstName"]
        response = requests.post(self.path, data={"login": login, "password": password, "firstName": first_name})
        assert response.json()['message'] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Запрос на создание курьера с незаполненным обязательным полем возвращает ошибку')
    @allure.step(f'Отправить POST запрос на эндпоинт {Endpoints.CREATE_COURIER} с незаполненным логином и/или паролем')
    @pytest.mark.parametrize(
        'payload',
        [
            pytest.param(Courier.courier_data_without_login, id="without_login"),
            pytest.param(Courier.courier_data_without_password, id="without_password"),
            pytest.param(Courier.courier_data_without_log_pas, id="without_log_pas")
        ])
    def test_create_courier_without_required_field(self, payload):
        response = requests.post(self.path, data=payload)
        assert response.status_code == 400

    @allure.title('Запрос на создание курьера с заполненными обязательными полями возвращает код 201')
    @allure.step(f'Отправить POST запрос на эндпоинт {Endpoints.CREATE_COURIER} с заполненным логином и паролем')
    def test_create_courier_with_required_fields(self, payload_create_courier):
        login = payload_create_courier["login"]
        password = payload_create_courier["password"]
        first_name = ""
        response = requests.post(self.path, data={"login": login, "password": password, "firstName": first_name})
        assert response.status_code == 201
