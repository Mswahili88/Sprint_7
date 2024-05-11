
class TestDataBody:

    BODY_WITHOUT_LOGIN = {"login": "",
                          "password": "111222333",
                          "firstName": "Петя"
                          }

    params_order_keys = 'firstName,lastName,address,metroStation,phone,rentTime,deliveryDate,comment,color'
    params_order_values = [
        ["Naruto", "Uchiha", "Konoha, 142 apt.", 4, "+7 800 355 35 35", 5, "2024-06-06", "пива", ["BLACK"]],
        ["Naruto", "Uchiha", "Konoha, 142 apt.", 4, "+7 800 355 35 35", 5, "2024-06-06", "пива", ["BLACK", "GREY"]],
        ["Naruto", "Uchiha", "Konoha, 142 apt.", 4, "+7 800 355 35 35", 5, "2024-06-06", "пива", []]
    ]

