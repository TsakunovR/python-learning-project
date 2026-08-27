import pytest
import requests


BASE_URL = "https://petstore.swagger.rv-school.ru/api/v3"


def test_add_pet():
    request_body = {
        "id": 1,
        "name": "Buddy",
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
    response = requests.post(
        url=f"{BASE_URL}/pet",
        json=request_body,
    )

    response_json = response.json()

    assert response.status_code == 200
    assert response_json["status"] == "available"
    assert response_json["id"] == 1
    assert response_json["name"] == "Buddy"