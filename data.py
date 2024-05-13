
class TestDataBody:

    BODY_WITHOUT_LOGIN = {"login": "",
                          "password": "111222333",
                          "firstName": "Петя"
                          }

    courier_same_name_409_text = 'Этот логин уже используется. Попробуйте другой.'
    courier_without_login_400_text = 'Недостаточно данных для создания учетной записи'
    login_without_login_400_text = 'Недостаточно данных для входа'
    login_without_reg_404_text = 'Учетная запись не найдена'

    params_order_keys = 'firstName,lastName,address,metroStation,phone,rentTime,deliveryDate,comment,color'
    params_order_values = [
        ["Naruto", "Uchiha", "Konoha, 142 apt.", 4, "+7 800 355 35 35", 5, "2024-06-06", "пива", ["BLACK"]],
        ["Naruto", "Uchiha", "Konoha, 142 apt.", 4, "+7 800 355 35 35", 5, "2024-06-06", "пива", ["BLACK", "GREY"]],
        ["Naruto", "Uchiha", "Konoha, 142 apt.", 4, "+7 800 355 35 35", 5, "2024-06-06", "пива", []]
    ]

