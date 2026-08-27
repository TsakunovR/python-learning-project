import requests

BASE_URL = "https://petstore.swagger.rv-school.ru/api/v3"

def test_create_new_pet():
    request_body = {
        "id": 1,
        "name": "Buddy",
        "status": "available"
    }

    response = requests.post (
        url=f"{BASE_URL}/pet",
        json=request_body
    )

    response_json = response.json()

    assert response.status_code == 200
    assert response_json["id"] == 1
    assert response_json["name"] == "Buddy"
    assert response_json["status"] == "available"