"""Пример тестов для функций из main.py."""

import pytest  # Библиотека для запуска тестов: ищет функции с именем test_* и выполняет их.
import requests
from main import add  # Импортируем функцию add из основного модуля, чтобы проверить её в тесте.


# Имя функции должно начинаться с test_ — тогда pytest найдёт и запустит этот тест.
def test_add_positive_numbers() -> None:
    """Проверяет сложение двух положительных чисел."""
    assert add(2, 3) == 5  # assert проверяет: если выражение ложно, тест падает с ошибкой.

def test_add_negative_numbers() -> None:
    """Проверяет сложение двух отрицательных чисел."""
    assert add(-2, -3) == -5
    assert add(-10, -5) == -15

def test_add_negative_and_positive() -> None:
    """Проверяет сложение отрицательного и положительного чисел."""
    assert add(-1, 6) == 5
    assert add(-5, 3) == -2
    assert add(-10, 10) == 0

BASE_URL = "https://petstore.swagger.rv-school.ru/api/v3"


def test_create_new_pet():
    request_body = {
        "id": 987,
        "name": "Gaby",
        "status": "available"
    }

    response = requests.post(
        url=f"{BASE_URL}/pet",
        json=request_body
    )

    response_json = response.json()

    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    assert response_json["id"] == 987, f"Ожидался id = 987, получен {response_json['id']}"
    assert response_json["name"] == "Gaby", f"Ожидалось имя Buddy, получено {response_json['name']}"
    assert response_json["status"] == "available", f"Ожидался статус available, получен {response_json['status']}"

