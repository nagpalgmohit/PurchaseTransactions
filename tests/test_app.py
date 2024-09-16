import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_save_txt_success(client):
    data = {
        "username": "xyz",
        "item_id": 10,
        "purchase_price": 23.55
    }
    response = client.post('/savetxn', json=data)
    assert response.status_code == 201
    assert response.json['message'] == "Transaction saved successfully"

def test_save_txn_invalid_username(client):
    data = {
        "username": "12345",
        "item_id": 123,
        "purchase_price": 20.55
    }
    response = client.post('/savetxn', json=data)
    assert response.status_code == 400
    assert response.json['message'] == "The username must adhere to the following criteria: It can consist of alphanumeric characters, alphabets, or be in email format. It cannot consist solely of digits or spaces."

def test_get_txn(client):
    data = {
        "username": "abc",
        "item_id": 123,
        "purchase_price": 37.65
    }
    client.post('/savetxn', json=data)

    response = client.get('/gettxn/abc')
    assert response.status_code == 200
    assert response.json[0]['username'] == "abc"
