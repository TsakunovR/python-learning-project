"""Пример тестов для функций из main.py."""

import pytest  # Библиотека для запуска тестов: ищет функции с именем test_* и выполняет их.
import requests

from main import add  # Импортируем функцию add из основного модуля, чтобы проверить её в тесте.


# Имя функции должно начинаться с test_ — тогда pytest найдёт и запустит этот тест.
def test_add_positive_numbers() -> None:
    """Проверяет сложение двух положительных чисел."""
    assert add(2, 3) == 5  # assert проверяет: если выражение ложно, тест падает с ошибкой.

def test_add_negative_with_positive_numbers() -> None:
    """Проверяет сложение негативного и позитивного чисел"""
    assert add(-3, 7) == 4

def test_add_negative_with_negative_numbers() -> None:
    """Проверяет сложение двух негативных чисел"""
    assert add(-3, -7) == -10

BASE_URL = "https://petstore.swagger.rv-school.ru/api/v3"

def test_create_new_pets():
    requests_body = {
  "id": 10,
  "name": "Buddy",
  "status": "available"
}
    response = requests.post(
        url=f"{BASE_URL}/pet",
        json=requests_body
    )

    response_json = response.json()

    assert response.status_code == 200
    assert response_json["id"] == 10
    assert response_json["name"] == "Buddy"
    assert response_json["status"] == "available"



