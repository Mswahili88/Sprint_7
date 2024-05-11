import allure
import requests
import urls
from data import TestDataBody

class TestCreateCourier:
    @allure.title('Создание курьера')
    @allure.description('Проверяем успешное создание курьера и в ответ статус 201 и тело ответа {"ok":true}')
    def test_create_courier(self, default_courier):
        payload = default_courier
        id_number = (requests.post(urls.URL_BASE + urls.URL_LOGIN, data=payload)).json()["id"]
        requests.delete(f"{urls.URL_BASE}{urls.URL_DELETE_COURIER}{id_number}")
        response = requests.post(urls.URL_BASE + urls.URL_CREATE_COURIER, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Создание курьера с уже существующим логином')
    @allure.description('Проверяем, что нельзя создать "дубль" существующего курьера. Ожидаем в ответ 409 и соответствующее письменное уведомление')
    def test_courier_same_name(self, default_courier):
        payload = default_courier
        response = requests.post(urls.URL_BASE + urls.URL_CREATE_COURIER, data=payload)
        assert response.status_code == 409 and response.json()["message"] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Создание курьера без одного из обязательных параметров')
    @allure.description('Проверяем, что нельзя создать курьера без логина и ожидаем ошибку 400 и соответствующее письменное уведомление')
    def test_courier_without_login(self):
        response = requests.post(urls.URL_BASE + urls.URL_CREATE_COURIER, data=TestDataBody.BODY_WITHOUT_LOGIN)
        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для создания учетной записи'