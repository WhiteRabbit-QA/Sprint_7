import helpers


class Courier:
    courier_data_without_login = {
        "login": "",
        "password": helpers.generate_random_string(7),
        "firstName": helpers.generate_random_string(7)
    }

    courier_data_without_password = {
        "login": helpers.generate_random_string(7),
        "password": "",
        "firstName": helpers.generate_random_string(7)
    }

    courier_data_without_log_pas = {
        "login": "",
        "password": "",
        "firstName": helpers.generate_random_string(7)
    }


class Login:
    payload_without_login = {
        "login": "",
        "password": helpers.generate_random_string(7)
    }

    payload_without_password = {
        "login": helpers.generate_random_string(7),
        "password": ""
    }


class Order:
    payload_order = {
        "firstName": helpers.generate_random_string(10),
        "lastName": helpers.generate_random_string(10),
        "address": "Ворошилова 5-23",
        "metroStation": 4,
        "phone": "+79273553535",
        "rentTime": 5,
        "deliveryDate": "2024-03-06",
        "comment": "some comment",
        "color": []
    }
