import sender_stand_request

# Проверка - 200 код ответа
def test_order_status_code():
    response = sender_stand_request.get_order()
    assert response.status_code == 200

# Чачин Александр, 9-я когорта — Финальный проект. Инженер по тестированию плюс