import data
import requests
import configuration

# Запрос на создание заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH)

# Сохранение трека заказа
def get_track():
    data.orders_body.copy()
    order = post_new_order()
    return order.json()["track"]

#Запрос на получение заказа по номеру трека
def get_order():
    track: object = get_track()
    params_track = {"t": track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH, params=params_track)