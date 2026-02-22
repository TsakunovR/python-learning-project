from http.client import responses
from urllib import response

import requests


BASE_URL = "https://petstore.swagger.rv-school.ru/api/v3"


def test_add_new_pet():
    request_body = {
        "id": 1,
        "name": "Buddy",
        "status": "available",
    }

    response = requests.post(
        url=f"{BASE_URL}/pet",
        json=request_body
    )

    response_json = response.json()
    assert response.status_code
    assert response_json["id"] == 1
    assert response_json["name"] == "Buddy"
    assert response_json["status"] == "available"

