class Transaction:
    def __init__(self, username, item_id, purchase_price):
        self.username = username
        self.item_id = item_id
        self.purchase_price = "{:.2f}".format(float(purchase_price))
