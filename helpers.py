import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_courier_correct_data():
    correct_courier_data = {
        "login": generate_random_string(7),
        "password": generate_random_string(7),
        "firstName": generate_random_string(7)
    }
    return correct_courier_data


def generate_wrong_login(login):
    wrong_login = login + generate_random_string(3)
    return wrong_login
