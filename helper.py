import random
import string
import allure

class TestMethodsHelper:
    @staticmethod
    @allure.step('Создание рандомных регистрационных данных')
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
