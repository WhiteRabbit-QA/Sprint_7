import allure
import pytest
import requests
import helpers
import source
from data import Login
from url import Url
from endpoints import Endpoints


class TestLoginCourier:
    path = f"{Url.URL_SERVICE}{Endpoints.LOGIN_COURIER}"

    @allure.title('Запрос на авторизацию с заполненными обязательными полями возвращает код 200')
    @allure.step(f'Отправить POST запрос на эндпоинт {Endpoints.LOGIN_COURIER} с заполненными логином и паролем')
    def test_login_with_required_fields(self, create_new_courier):
        payload = {"login": create_new_courier[0], "password": create_new_courier[1]}
        response = requests.post(self.path, data=payload)
        assert response.status_code == 200

    @allure.title('Успешный запрос возвращает "id" курьера')
    @allure.step(f'Отправить POST запрос на эндпоинт {Endpoints.LOGIN_COURIER} для авторизации')
    def test_login_successful_return_id(self, create_new_courier):
        payload = {"login": create_new_courier[0], "password": create_new_courier[1]}
        response = requests.post(self.path, data=payload)
        assert "id" in response.text

    @allure.title('Запрос на авторизацию с незаполненным обязательным полем возвращает ошибку')
    @allure.step(f'Отправить POST запрос на эндпоинт {Endpoints.LOGIN_COURIER} с незаполненными логином или паролем')
    @pytest.mark.parametrize(
        'payload',
        [
            pytest.param(Login.payload_without_password, id='without_password'),
            pytest.param(Login.payload_without_login, id='without_login')
        ])
    def test_login_without_required_fields(self, payload):
        response = requests.post(self.path, data=payload)
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Запрос на авторизацию с неверным логином возвращает код 404')
    @allure.step(f'Отправить POST запрос на эндпоинт {Endpoints.LOGIN_COURIER} с неверным логином')
    def test_login_with_wrong_login(self, create_new_courier):
        payload = {"login": helpers.generate_wrong_login(create_new_courier[0]), "password": create_new_courier[1]}
        response = requests.post(self.path, data=payload)
        assert response.status_code == 404

    @allure.title('Запрос на авторизацию с несуществующим пользователем возвращает ошибку')
    @allure.step(f'Отправить POST запрос на эндпоинт {Endpoints.LOGIN_COURIER} с несуществующим логином')
    def test_login_with_not_exist_user(self):
        user = source.register_new_courier_and_return_login_password()
        id_user = source.get_id_courier(user[0], user[1])
        source.delete_courier(id_user)
        payload = {"login": user[0], "password": user[1], "firstName": user[2]}
        response = requests.post(self.path, data=payload)
        assert response.status_code == 404
