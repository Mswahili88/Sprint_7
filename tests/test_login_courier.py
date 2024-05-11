import allure
import requests
import helper
import urls
from data import TestDataBody

class TestLoginCourier:

    @allure.title('Успешный логин курьера')
    @allure.description('Проверяем, что происходит успешный логин курьера с ответом 200 и приходит его id, который не пустой')
    def test_success_login(self, default_courier):
        payload = default_courier
        response = requests.post(urls.URL_BASE + urls.URL_LOGIN, data=payload)
        assert response.status_code == 200 and response.json()["id"] is not None

    @allure.title('Логин курьером без одного из обязательных к заполнению полей')
    @allure.description('Проверяем, что нельзя залогиниться без логина, что приходит ожидаемый статус 400 и соответствующее письменное уведомление')
    def test_login_with_empty_data(self):
        response = requests.post(urls.URL_BASE + urls.URL_LOGIN, data=TestDataBody.BODY_WITHOUT_LOGIN)
        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для входа'

    @allure.title('Логин курьером с несуществующими данными')
    @allure.description('Проверяем, что нельзя залогиниться несуществующими курьером, допустим, в логине, и что приходит ответ 404 с соответствующим письменным уведомлением')
    def test_login_without_registration(self):
        payload = helper.TestMethodsHelper.create_random_login_password()
        response = requests.post(urls.URL_BASE + urls.URL_LOGIN, data=payload)
        assert response.status_code == 404 and response.json()["message"] == 'Учетная запись не найдена'