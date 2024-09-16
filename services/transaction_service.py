import os


class TransactionService:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_transaction(self, transaction, file_lock):
        try:
            with file_lock:
                with open(self.file_path, 'a') as file:
                    file.write(f'{transaction.username},{transaction.item_id},{transaction.purchase_price}\n')
            return True, "Transaction saved successfully"
        except Exception as e:
            return False, f"Error saving transaction: {str(e)}"

    def get_transactions(self, value, file_lock):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("Purchases file not found")

        results = []
        try:
            with file_lock: 
                with open(self.file_path, 'r') as file:
                    for line in file:
                        username, item_id, purchase_price = line.strip().split(',')
                        if value == username or value == item_id or value == purchase_price:
                            results.append({
                                'username': username,
                                'item_id': item_id,
                                'purchase_price': purchase_price
                            })

            if results:
                return results, None
            else:
                return None, "No matching transactions found"
        except Exception as e:
            return None, f"Error retrieving transactions: {str(e)}"
