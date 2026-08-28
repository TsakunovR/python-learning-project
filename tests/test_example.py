"""Пример тестов для функций из main.py."""

import pytest  # Библиотека для запуска тестов: ищет функции с именем test_* и выполняет их.
import requests

from main import add  # Импортируем функцию add из основного модуля, чтобы проверить её в тесте.
from tests.DZ import BASE_URL


# Имя функции должно начинаться с test_ — тогда pytest найдёт и запустит этот тест.
def test_add_positive_numbers() -> None:
    """Проверяет сложение двух положительных чисел."""
    assert add(2, 3) ==5 # assert проверяет: если выражение ложно, тест падает с ошибкой.


def test_add_negative_numbers() -> None:
    """Проверяет сложение двух отрицательных чисел"""
    assert add(-7, -7) == -14

BASE_URL = "https://petstore.swagger.rv-school.ru/api/v3"

def test_create_Store_order():
    request_body = {
  "id": 10,
  "petId": 198772,
  "quantity": 7,
  "shipDate": "2026-08-28T12:26:11.889Z",
  "status": "approved",
  "complete": True
}
    response = requests.post(
        url=f"{BASE_URL}/store/order",
        json=request_body
    )

    response_json = response.json()
    assert response.status_code
    assert response_json["status"] == "approved"
    assert response_json["id"] == 10
    assert response_json["petId"] == 198772
    assert response_json["quantity"] == 7
    assert response_json["complete"] is True
