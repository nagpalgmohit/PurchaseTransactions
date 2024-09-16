# PurchaseTransactions
This project implements a RESTful API using Flask for managing purchase transactions. The API allows users to save and retrieve purchase transaction data, including username, item_id, and purchase_price. Transaction records are stored in a local text file (purchases.txt), and the system supports input data validation.

**Features**
1. **Save Transaction:** Store purchase transactions with validated username, item_id, and purchase_price.
2. **Retrieve Transaction:** Fetch transaction data by searching for a specific username, item_id, or purchase_price.
3. **Input Validation:** Ensures data integrity through comprehensive validation checks.
4. **Concurrent Access:** Implements threading locks for safe concurrent read and write operations.
5. **Dependency Management:** Includes Pipfile and Pipfile.lock for proper package management.

**Technical Details**
1. **JSON Schema Validation:** Utilizes the jsonschema library to validate incoming JSON data against a predefined schema.
2. **Thread Safety:** Implements Python's threading.Lock() to prevent data corruption and ensure thread-safe access to shared resources.
3. **File-based Storage:** Transactions are stored in purchases.txt.

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

Validation Criteria:
1. JSON Schema: Validates incoming JSON data against a predefined schema,
2. Username: Alphanumeric, alphabets, or email format. No spaces or digits-only allowed.
3. Item ID: Positive integer.
4. Purchase Price: Positive decimal number. 

If the validations are passed the information will be stored in a text file called purchases.txt  
xyz,101,59.99  

2. **Retrieve Transaction**  
Fetches transactions based on the given username, item_id, or purchase_price.  
GET http://127.0.0.1:5000/gettxn/<value>  
You can provide one of the following values: username, item_id, or purchase_price.  
Example:  
GET http://127.0.0.1:5000/gettxn/xyz  
GET http://127.0.0.1:5000/gettxn/101  
GET http://127.0.0.1:5000/gettxn/59.99  
Any of the above will return the below JSON object:  
[  
{  
    "username": "xyz",  
    "item_id": 101,  
    "purchase_price": 59.99  
}  
]  

**Installation on macOS**
1. Clone repository: git clone https://github.com/nagpalgmohit/PurchaseTransactions.git
2. Install pipenv: pip install pipenv --user
3. Install dependencies: pipenv install --ignore-pipfile
4. Run the application file: pipenv run python app.py
5. To run tests: export PYTHONPATH=$(pwd)  
pipenv run pytest

**Limitations**  
Authentication and authorization are not implemented in this version.
