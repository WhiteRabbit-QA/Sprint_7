import requests
import helpers


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    login_pass = []

    login = helpers.generate_random_string(10)
    password = helpers.generate_random_string(10)
    first_name = helpers.generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


def get_id_courier(login, password):
    payload = {"login": login, "password": password}
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload).json()
    courier_id = response["id"]
    return courier_id


def delete_courier(courier_id):
    requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')
