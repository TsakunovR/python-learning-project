import requests

BASE_URL = "https://petstore.swagger.rv-school.ru/api/v3"

def test_create_new_pet():
    request_body = {
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

    response = requests.post (
        url=f"{BASE_URL}/pet",
        json=request_body
    )

    response_json = response.json()

    assert response.status_code == 200
    assert response_json["id"] == 10
    assert response_json["name"] == "doggie"
    assert response_json["category"]["id"] == 1
    assert response_json["category"]["name"] == "Dogs"
    assert response_json["photoUrls"][0] == "string"
    assert response_json["tags"][0]["id"] == 0
    assert response_json["tags"][0]["name"] == "string"
    assert response_json["status"] == "available"