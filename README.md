# PurchaseTransactions
This project implements a RESTful API using Flask for managing purchase transactions. The API allows users to save and retrieve purchase transaction data such as username, item_id, and purchase_price. The system stores transaction records in a local text file (purchases.txt) and supports validation for the input data. Authentication and authorization are not in the scope of the project.

**Features**
1. **Save Transaction:** Allows users to save a purchase transaction with validation for username, item_id, and purchase_price.
2. **Retrieve Transaction:** Allows users to retrieve transaction data by searching for a specific username, item_id, or purchase_price.
3. **Validation:**
a. username: Can be alphanumeric, alphabets, or in email format but must not consist solely of digits or spaces.
b. item_id: Must be a positive integer.
c. purchase_price: Must be a positive decimal number.
d. schema validaton: The JSON schema validates that username is a string, item_id is an integer, and purchase_price is a number. It also ensures that all three fields are present in the POST request. If any additional properties are provided beyond these, the schema detects them and returns an additionalProperties error.
5. **File-based Storage:** Transactions are stored in purchases.txt.

**Requirements**
1. Python 3.x
2. Pip
3. Postman

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

If the validations are passed the information will be stored in a text file called purchases.txt  
xyz,101,59.99  

2. **Retrieve Transaction**  
Retrieve transactions based on the given username, item_id, or purchase_price.  
GET http://127.0.0.1:5000/gettxn/<value>  
You can provide one of the following values: username, item_id, or purchase_price. A search will be conducted in the purchases.txt file, and all matching entries will be returned.  
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



