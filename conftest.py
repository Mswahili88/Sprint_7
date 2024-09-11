import allure
import pytest
import requests
import urls
import helper

@allure.step('Создание нового курьера и удаление данных о курьере в конце теста')
@pytest.fixture(scope='function')
def default_courier():
    payload = helper.TestMethodsHelper.create_random_login_password()
    yield payload
    response_id = requests.post(urls.URL_BASE + urls.URL_LOGIN, data=payload)
    id_number = response_id.json()["id"]
    requests.delete(f"{urls.URL_BASE}{urls.URL_DELETE_COURIER}{id_number}")













