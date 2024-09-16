import pytest
from validators.transaction_validator import TransactionValidator

@pytest.mark.parametrize("item_id,expected", [
    (123, (True, None)),
    (0, (False, "Item id cannot be empty or zero.")),
    (None, (False, "Item id cannot be empty or zero.")),
    (-5, (False, "The item id must adhere to the following criteria: It can consist of only positive digits. It cannot consist of decimals, negatives or zero.")),
    ('abc', (False, "The item id must adhere to the following criteria: It can consist of only positive digits. It cannot consist of decimals, negatives or zero.")),
])
def test_validate_item_id(item_id, expected):
    assert TransactionValidator.validate_item_id(item_id) == expected

@pytest.mark.parametrize("username,expected", [
    ('john_doe', (True, None)),
    ('john.doe@example.com', (True, None)),
    ('12345', (False, "The username must adhere to the following criteria: It can consist of alphanumeric characters, alphabets, or be in email format. It cannot consist solely of digits or spaces.")),
    ('', (False, "Username cannot be empty.")),
    ('   ', (False, "The username must adhere to the following criteria: It can consist of alphanumeric characters, alphabets, or be in email format. It cannot consist solely of digits or spaces.")),
])
def test_validate_username(username, expected):
    assert TransactionValidator.validate_username(username) == expected

@pytest.mark.parametrize("purchase_price,expected", [
    (10.00, (True, None)),
    (5.50, (True, None)),
    ('12.34', (True, None)),
    (0, (False, "Purchase price cannot be empty or zero.")),
    ('10', (True, None)),
    (-10, (False, "The purchase price must adhere to the following criteria: It can consist of only positive digits with decimals. It cannot consist of negatives or zero.")),
])
def test_validate_purchase_price(purchase_price, expected):
    assert TransactionValidator.validate_purchase_price(purchase_price) == expected

schema = {
    'type': 'object',
    'properties': {
        'username': {'type': 'string'},
        'item_id': {'type': 'integer'},
        'purchase_price': {'type': 'number'}
    },
    'required': ['username', 'item_id','purchase_price'],
    'additionalProperties': False
}

error_messages = {
    'required': "The field '{field}' is required.",
    'type': "The field '{field}' should be of type '{type}'.",
    'additionalProperties': "The field '{field}' is not allowed."
}

@pytest.mark.parametrize("data, expected_output", [
    # Test case where validation passes
    ({"username": "testuser", "item_id": 1, "purchase_price": 25.99}, (True, None)),

    # Test case where 'username' is missing
    ({"item_id": 1, "purchase_price": 25.99}, 
     (False, "The field 'username' is required.")),

    # Test case where 'item_id' is not the correct type
    ({"username": "testuser", "item_id": "wrong_type", "purchase_price": 25.99}, 
     (False, "The field 'item_id' should be of type 'integer'.")),

    # Test case where additional properties are present
    ({"username": "testuser", "item_id": 1, "purchase_price": 25.99, "extra_field": "not_allowed"}, 
     (False, "The field 'extra_field' is not allowed.")),

])
def test_validate_json(data, expected_output):
    result = TransactionValidator.validate_json(data, error_messages, schema)
    assert result == expected_output
