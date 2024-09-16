# PurchaseTransactions
This project implements a RESTful API using Flask for managing purchase transactions. The API allows users to save and retrieve purchase transaction data such as username, item_id, and purchase_price. The system stores transaction records in a local text file (purchases.txt) and supports validation for the input data.

**Features**
1. **Save Transaction:** Allows users to save a purchase transaction with validation for username, item_id, and purchase_price.
2. **Retrieve Transaction:** Allows users to retrieve transaction data by searching for a specific username, item_id, or purchase_price.
3. **Validation:**
username: Can be alphanumeric, alphabets, or in email format but must not consist solely of digits or spaces.
item_id: Must be a positive integer.
purchase_price: Must be a positive decimal number.
4. **File-based Storage:** Transactions are stored in purchases.txt.

**Requirements**
Python 3.x
Pip
Postman

**Usage**
1. **Save Transaction**
Saves a new transaction to the purchases.txt file.

POST http://127.0.0.1:5000/savetxn
Content-Type: application/json

{
    "username": "xyz",
    "item_id": 101,
    "purchase_price": 59.99
}
Validation Criteria
Username: Must be alphanumeric, alphabets, or in email format. No spaces or only digits are allowed.
Item ID: Must be a positive integer.
Purchase Price: Must be a decimal number.

If the validations are passed the information will be store in a text file called purchases.txt
xyz,101,59.99

2. **Retrieve Transaction**
Retrieve transactions based on the given username, item_id, or purchase_price.

GET http://127.0.0.1:5000/gettxn/<value>

In place of value, you can give either one of the following username, item_id, or purchase_price.
A search will be initiated in purchases.txt and all matched rows will be returned

GET http://127.0.0.1:5000/gettxn/xyz
GET http://127.0.0.1:5000/gettxn/101
GET http://127.0.0.1:5000/gettxn/59.99

**Installation on macOS**
1. Clone repository: git clone https://github.com/nagpalgmohit/PurchaseTransactions.git
2. Install pipenv: pip install pipenv --user
3. Install dependencies: pipenv install --ignore-pipfile
4. Run the application file: pipenv run python app.py
5. To run tests: export PYTHONPATH=$(pwd)
pipenv run pytest



