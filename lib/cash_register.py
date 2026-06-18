#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self._transactions = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.total = round(self.total, 2)
        for _ in range(quantity):
            self.items.append(title)
        self._transactions.append((title, price, quantity))

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = round(self.total * (1 - self.discount / 100), 2)
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        if self._transactions:
            title, price, quantity = self._transactions.pop()
            self.total -= price * quantity
            self.total = round(self.total, 2)
            for _ in range(quantity):
                self.items.remove(title)