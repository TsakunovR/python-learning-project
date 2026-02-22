"""Пример тестов для функций из main.py."""

import pytest  # Библиотека для запуска тестов: ищет функции с именем test_* и выполняет их.
import requests

from main import add  # Импортируем функцию add из основного модуля, чтобы проверить её в тесте.


# Имя функции должно начинаться с test_ — тогда pytest найдёт и запустит этот тест.
def test_add_positive_numbers() -> None:
    """Проверяет сложение двух положительных чисел."""
    assert add(2, 3) == 5  # assert проверяет: если выражение ложно, тест падает с ошибкой.

def test_add_negative_numbers() -> None:
    assert add(-1, 6) == 5


BASE_URL = "https://petstore.swagger.rv-school.ru/api/v3"

def test_ceate_Store_order():
    reguest_body = {
        "id": 10,
        "petId": 198772,
        "quantity": 7,
        "shipDate": "2026-02-22T08:21:55.657Z",
        "status": "approved",
        "complete": True
    }

    response = requests.post(
        url=f"{BASE_URL}/store/order",
        json=reguest_body
    )

    response_json = response.json()

    assert response.status_code
    assert response_json['id'] == 10
    assert response_json['petId'] == 198772
    assert response_json['quantity'] == 7
    assert response_json['status'] == 'approved'
    assert response_json['complete'] == True


def test_create_New_pet():
    reguest_body = {
        "id": 1,
        "name": "Buddy",
        "status": "available"
    }
    response = requests.post(
        url=f"{BASE_URL}/pet",
        json=reguest_body
    )
    response_json = response.json()

    assert response.status_code
    assert response_json['id'] == 1
    assert response_json['name'] == 'Buddy'
    assert response_json['status'] == 'available'
