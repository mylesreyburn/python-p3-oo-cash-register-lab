#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount = 0) -> None:
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, item, price, quantity = 1):
    self.total += (price * quantity)
    self.last_price = price * quantity
    i = 0
    while i < quantity:
      self.items.append(item)
      i += 1

  def apply_discount(self):
    if self.discount > 0:
      self.total = self.total * (1 - (self.discount/100))
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
  
  def void_last_transaction(self):
    self.total -= self.last_price

  # def add_item(self, item, price, quantity = 1):
  #   print(self.total)
  #   print(self.prices)
  #   i = 0
  #   while i < quantity:
  #     self.items.append(item)
  #     self.prices.append(price)
  #     i += 1
  #   for cost in self.prices:
  #     self.total += cost