from flask import Flask, request, jsonify, abort
from services.transaction_service import TransactionService
from validators.transaction_validator import TransactionValidator
from models.transaction import Transaction
import os
from flask_expects_json import expects_json
from threading import Lock


app = Flask(__name__)
file_lock = Lock()

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


file_path = 'purchases.txt'


@app.route('/savetxn', methods=['POST'])
def save_txt():
    data = request.json
    valid, error_message = TransactionValidator.validate_json(data, error_messages, schema)
    if not valid:
        return jsonify({"error": error_message}), 400

    
    username = data.get('username')
    item_id = data.get('item_id')
    purchase_price = data.get('purchase_price')

    valid_item_id, error_item_id = TransactionValidator.validate_item_id(item_id)
    if not valid_item_id:
        return jsonify({"message": error_item_id}), 400

    valid_username, error_username = TransactionValidator.validate_username(username)
    if not valid_username:
        return jsonify({"message": error_username}), 400

    valid_purchase_price, error_purchase_price = TransactionValidator.validate_purchase_price(purchase_price)
    if not valid_purchase_price:
        return jsonify({"message": error_purchase_price}), 400

    
    transaction = Transaction(username, item_id, purchase_price)
    service = TransactionService(file_path)
    success, message = service.save_transaction(transaction, file_lock)

    if success:
        return jsonify({"message": message}), 201
    else:
        abort(500, description=message)



@app.route('/gettxn/<value>', methods=['GET'])
def get_txt(value):
    service = TransactionService(file_path)
    try:
        results, error = service.get_transactions(value, file_lock)
        if results:
            return jsonify(results), 200
        else:
            return jsonify({"message": error}), 404
    except Exception as e:
        abort(500, description=f"Error retrieving transactions: {str(e)}")


if __name__ == '__main__':
    app.run()
