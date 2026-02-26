#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Validate discount on initialization
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")
            self._discount = 0

        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    # Property for discount with validation
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        # Update total
        self.total += price * quantity
        # Add items to items list
        for _ in range(quantity):
            self.items.append(item)
        # Record transaction
        self.previous_transactions.append({"item": item, "price": price, "quantity": quantity})

    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total * (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
            if self.previous_transactions:
                self.previous_transactions.pop()  # remove last transaction
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.previous_transactions:
            last = self.previous_transactions.pop()
            self.total -= last["price"] * last["quantity"]
            # Remove items from items list
            for _ in range(last["quantity"]):
                if last["item"] in self.items:
                    self.items.remove(last["item"])