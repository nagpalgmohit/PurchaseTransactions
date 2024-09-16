import pytest
import os
from services.transaction_service import TransactionService
from models.transaction import Transaction
from threading import Lock
file_lock = Lock()

@pytest.fixture
def test_file(tmpdir):
    # Temporary file path for testing
    return os.path.join(tmpdir, 'purchases.txt')

def test_save_transaction(test_file):
    service = TransactionService(test_file)
    transaction = Transaction("mno",57,18.75)
    success, message = service.save_transaction(transaction, file_lock)
    
    assert success == True
    assert message == "Transaction saved successfully"

    # Check if the file is written correctly
    with open(test_file, 'r') as file:
        lines = file.readlines()
        assert len(lines) == 1
        assert lines[0] == "mno,57,18.75\n"

def test_get_transactions(test_file):
    service = TransactionService(test_file)
    transaction = Transaction("def@hij.com",77,89.99)
    service.save_transaction(transaction, file_lock)
    
    # Get the transaction by username
    results, error = service.get_transactions("def@hij.com", file_lock)
    assert len(results) == 1
    assert results[0]['username'] == "def@hij.com"
    assert results[0]['item_id'] == "77"
    assert results[0]['purchase_price'] == "89.99"

    # Get the transaction by item_id
    results, error = service.get_transactions("77", file_lock)
    assert len(results) == 1
    assert results[0]['username'] == "def@hij.com"
    assert results[0]['item_id'] == "77"

    # Check for non-existent data
    results, error = service.get_transactions("1.75", file_lock)
    assert results == None
    assert error == "No matching transactions found"
