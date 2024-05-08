
class TestDataBody:
    BODY_MAIN_DATA = {"login": "vvp88",
                      "password": "111222333",
                       "firstName": "vadim"
                       }

    BODY_WITHOUT_LOGIN = {"login": "",
                          "password": "111222333",
                          "firstName": "Петя"
                          }

    BODY_THE_SAME_DATA = {"login": "vvp88",
                          "password": "111222333",
                          "firstName": "vadim"
                          }

    BODY_CHECK_LOGIN = {"login": "vvp88",
                        "password": "111222333"
                        }

    BODY_LOGIN_ONLY = {"login": "vvp88",
                       "password": ""
                       }

    BODY_MISTAKE_IN_LOGIN = {"login": "vvp888",
                       "password": "111222333"
                       }

    params_order_keys = 'firstName,lastName,address,metroStation,phone,rentTime,deliveryDate,comment,color'
    params_order_values = [
        ["Naruto", "Uchiha", "Konoha, 142 apt.", 4, "+7 800 355 35 35", 5, "2024-06-06", "пива", ["BLACK"]],
        ["Naruto", "Uchiha", "Konoha, 142 apt.", 4, "+7 800 355 35 35", 5, "2024-06-06", "пива", ["BLACK", "GREY"]],
        ["Naruto", "Uchiha", "Konoha, 142 apt.", 4, "+7 800 355 35 35", 5, "2024-06-06", "пива", []]
    ]

