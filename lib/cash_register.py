#!/usr/bin/env python3

class CashRegister:
    """A simple CashRegister class"""

    def __init__(self, discount=0):
        if not isinstance(discount, int) or discount < 0 or discount > 100:
            print("Not valid discount")
            discount = 0

        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        """Add item to cart"""
        total_price = price * quantity
        self.total += total_price

        # Add multiple times based on quantity
        for _ in range(quantity):
          self.items.append(item)
        
        self.previous_transactions.append({
          "item": item,
          "price": price, 
          "quantity": quantity
        })

    def apply_discount(self):
        """Apply percentage discount"""
        if not self.previous_transactions or self.discount == 0:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        """Remove last transaction"""
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()

        item = last_transaction["item"]
        price = last_transaction["price"]
        quantity = last_transaction["quantity"]

        # Adjust total
        self.total -= price * quantity

        # Remove item from items list
        if item in self.items:
            self.items.remove(item)