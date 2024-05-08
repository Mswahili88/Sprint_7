import allure
import pytest
import requests
import urls
from data import TestDataBody

class TestCreateCourier:
    @allure.title('Создание курьера')
    @allure.description('Проверяем успешное создание курьера и в ответ статус 201 и тело ответа {"ok":true}')
    def test_create_courier(self, default_courier):
        response = default_courier
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Создание курьера с уже существующим логином')
    @allure.description('Проверяем, что нельзя создать "дубль" существующего курьера. Ожидаем в ответ 409 и соответствующее письменное уведомление')
    def test_courier_same_name(self, default_courier):
        response = requests.post(urls.URL_CREATE_COURIER, data=TestDataBody.BODY_THE_SAME_DATA)
        assert response.status_code == 409 and response.json()["message"] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Создание курьера без одного из обязательных параметров')
    @allure.description('Проверяем, что нельзя создать курьера без логина, ожидаем ошибку 400 и соответствующее письменное уведомление')
    def test_courier_without_login(self):
        response = requests.post(urls.URL_CREATE_COURIER, data=TestDataBody.BODY_WITHOUT_LOGIN)
        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для создания учетной записи'

class TestLoginCourier:

    @allure.title('Успешный логин курьера')
    @allure.description('Проверяем, что происходит успешный логин курьера с ответом 200 и приходит его id, который не пустой')
    def test_success_login(self, default_courier):
        response = requests.post(urls.URL_LOGIN, data=TestDataBody.BODY_CHECK_LOGIN)
        assert response.status_code == 200 and response.json()["id"] is not None

    @allure.title('Логин курьером без одного из обязательных к заполнению полей')
    @allure.description('Проверяем, что нельзя залогиниться без пароля, что приходит ожидаемый статус 400 и соответствующее письменное уведомление')
    def test_login_with_empty_data(self, default_courier):
        response = requests.post(urls.URL_LOGIN, data=TestDataBody.BODY_LOGIN_ONLY)
        assert response.status_code == 400 and response.json()["message"] == 'Недостаточно данных для входа'

    @allure.title('Логин курьером с ошибкой в данных')
    @allure.description('Проверяем, что нельзя залогиниться с ошибкой, допустим, в логине, и что приходит ответ 404 с соответствующим письменным уведомлением')
    def test_login_with_mistake(self, default_courier):
        response = requests.post(urls.URL_LOGIN, data=TestDataBody.BODY_MISTAKE_IN_LOGIN)
        assert response.status_code == 404 and response.json()["message"] == 'Учетная запись не найдена'

class TestMakeOrder:

    @allure.title('Проверка создания заказа')
    @allure.description('Проверяем через параметризацию возможность совершения заказа с указанием одного из цветов самоката, обоих цветов сразу и вообще без выбора цвета')
    @allure.description('В ответ убеждаемся в получении кода 201 и наличия слова "track" в теле ответа')
    @pytest.mark.parametrize(TestDataBody.params_order_keys, TestDataBody.params_order_values)
    def test_create_order(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color):
        payload = {'firstName': firstName, 'lastName': lastName, 'address': address,
                   'metroStation': metroStation, 'phone': phone, 'rentTime': rentTime,
                   'deliveryDate': deliveryDate, 'comment': comment, 'color': color}
        response = requests.post(urls.URL_CREATE_ORDER, json=payload)
        assert response.status_code == 201 and 'track' in response.text

    @allure.title('Проверка получения списка заказов')
    @allure.description('Получаем список заказов без id курьера и убеждаемся в наличии ответа 200, и что список заказов не пустой')
    def test_get_list_of_orders(self):
        response = requests.get(urls.URL_GET_ALL_ORDERS)
        assert response.status_code == 200 and response.json()["orders"] is not None
