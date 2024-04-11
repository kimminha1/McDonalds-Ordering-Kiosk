#Mcdonalds ordering kiosk project
#Mcdonalds.py:
class Item:
    def __init__(self, name, price, has_deal):
        self.name = name
        self.price = price
        self.has_deal = has_deal
#app.py:
from Mcdonalds import Item
fries = Item('fries', 1.50, True)
burger = Item('burger', 4, True)
icecream = Item('ice cream', 2, False)

subtotal = 0
order = input('Menu: fries, burger, ice cream.\nWhat would you like to order?')
if 'fries' in order:
    subtotal += fries.price
    if 'burger' in order:
        subtotal += burger.price
        if 'ice cream' in order:
            subtotal += icecream.price
elif 'burger' in order:
    subtotal += burger.price
    if 'ice cream' in order:
        subtotal += icecream.price
elif 'ice cream' in order:
        subtotal += icecream.price
print(f'Your total is ${subtotal}')