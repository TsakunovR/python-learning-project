"""Пример тестов для функций из main.py."""

import requests


# Имя функции должно начинаться с test_ — тогда pytest найдёт и запустит этот тест.
def test_add_positive_numbers() -> None:
    """Проверяет сложение двух положительных чисел."""
    assert add(2, 3) == 5  # assert проверяет: если выражение ложно, тест падает с ошибкой.

def test_add_negative_numbers() -> None:
    assert add(-2, -3) == 5

def test_add_different_numbers() -> None:
    assert add(-1, 2) == 1


def test_create_pet():
    # 1. Базовый URL и эндпоинт
    base_url = "https://petstore.swagger.rv-school.ru/api/v3"
    endpoint = "/pet"

    # 2. Тело запроса
    payload = {
        "id": 10,
        "name": "doggie",
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    # 3. Отправляем POST-запрос
    response = requests.post(f"{base_url}{endpoint}", json=payload)

    # 4. Проверяем статус-код
    expected_status = 200
    assert response.status_code == expected_status, f"Ожидался статус {expected_status}, но получили {response.status_code}"

    # 5. Распаковываем JSON-ответ обратно в питоновский словарь
    response_data = response.json()

    # 6. Проверки (Ассерты)
    # Базовые поля
    assert response_data["id"] == 10, "Неверный id"
    assert response_data["name"] == "doggie", "Неверное имя"
    assert response_data["status"] == "available", "Неверный статус"

    # Вложенный объект (category) - обращаемся последовательно по ключам
    assert response_data["category"]["id"] == 1, "Неверный id категории"
    assert response_data["category"]["name"] == "Dogs", "Неверное имя категории"

    # Массивы (photoUrls и tags) - сначала берем элемент по индексу [0], потом ключ
    assert response_data["photoUrls"][0] == "string", "Неверный photoUrl"
    assert response_data["tags"][0]["id"] == 0, "Неверный id тега"
    assert response_data["tags"][0]["name"] == "string", "Неверное имя тега"