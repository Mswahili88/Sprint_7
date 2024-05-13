import allure
import pytest
import requests
import urls
from data import TestDataBody

class TestMakeOrder:

    @allure.title('Проверка создания заказа')
    @allure.description('Проверяем через параметризацию возможность совершения заказа с указанием одного из цветов самоката, обоих цветов сразу и вообще без выбора цвета')
    @allure.description('В ответ убеждаемся в получении кода 201 и наличия слова "track" в теле ответа')
    @pytest.mark.parametrize(TestDataBody.params_order_keys, TestDataBody.params_order_values)
    def test_create_order(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color):
        payload = {'firstName': firstName, 'lastName': lastName, 'address': address,
                   'metroStation': metroStation, 'phone': phone, 'rentTime': rentTime,
                   'deliveryDate': deliveryDate, 'comment': comment, 'color': color}
        response = requests.post(urls.URL_BASE + urls.URL_CREATE_ORDER, json=payload)
        assert response.status_code == 201 and 'track' in response.text

    @allure.title('Проверка получения списка заказов')
    @allure.description('Получаем список заказов без id курьера и убеждаемся в наличии ответа 200, и что список заказов не пустой')
    def test_get_list_of_orders(self):
        response = requests.get(urls.URL_BASE + urls.URL_GET_ALL_ORDERS)
        assert response.status_code == 200 and response.json()["orders"] is not None
