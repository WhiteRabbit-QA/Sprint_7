import allure
import pytest
import requests
import helpers
import source
from endpoints import Endpoints
from url import Url


@allure.title('Сгенерировать логин, пароль, имя курьера')
@pytest.fixture
def payload_create_courier():
    payload_courier = helpers.generate_courier_correct_data()
    yield payload_courier
    payload_courier.clear()


@allure.title('Создать курьера')
@pytest.fixture
def create_new_courier():
    courier_data_list = source.register_new_courier_and_return_login_password()
    yield courier_data_list
    response = requests.post(f"{Url.URL_SERVICE}{Endpoints.LOGIN_COURIER}",
                             data={'login': courier_data_list[0], 'password': courier_data_list[1]}).json()
    id_courier = response['id']
    with allure.step('Удалить тестового курьера'):
        requests.delete(f"{Url.URL_SERVICE}{Endpoints.CREATE_COURIER}/{id_courier}")
