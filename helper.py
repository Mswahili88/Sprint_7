import requests
import random
import string
import allure

class TestMethodsHelper:
    @staticmethod
    @allure.step('Регистрация нового курьера с рандомными данными и возврат этих данных')
    def register_new_courier_and_return_login_password():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login_pass = {}

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        if response.status_code == 201:
           login_pass["login"] = login
           login_pass["password"] = password
           login_pass["firstName"] = first_name

        return login_pass

    @staticmethod
    @allure.step('Создание рандомных логина, пароля и имени')
    def create_random_login_password():

        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        login_pass = {"login": login, "password": password, "firstName": first_name}
        return login_pass
