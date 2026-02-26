#!/usr/bin/env python3

#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # discount percentage (e.g. 20 means 20%)
        self.discount = discount

        # total amount starts at 0
        self.total = 0

        # list of item titles
        self.items = []

        # track last transaction for voiding
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        """
        Adds an item (or multiple items) to the register.
        """
        transaction_total = price * quantity
        self.total += transaction_total
        self.last_transaction = transaction_total

        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        """
        Applies the discount to the total if available.
        """
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """
        Removes the last transaction from the total.
        """
        self.total -= self.last_transaction
        self.last_transaction = 0
