import allure
import pytest
import requests
import urls
from data import TestDataBody

@allure.step('Создание нового курьера и удаление данных о курьере в конце теста')
@pytest.fixture(scope='function')
def default_courier():
    response = requests.post(urls.URL_CREATE_COURIER, data=TestDataBody.BODY_MAIN_DATA)

    yield response


    response_id = requests.post(urls.URL_LOGIN, data=TestDataBody.BODY_CHECK_LOGIN)
    id_number = response_id.json()["id"]
    response_delete = requests.delete(f"{urls.URL_DELETE_COURIER}{id_number}")
    return response_delete










