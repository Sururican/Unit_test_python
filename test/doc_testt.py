# src/my_doctest.txt

"""
This is a doctest file for my_module.py.
>>> from src.shopping.py import ShoppingCart, Item
>>> cart = ShoppingCart()
>>> item1 = Item('Laptop', 1000)
>>> item2 = Item('mause', 100)
>>> cart.add_item(item1)
>>> cart.add_item(item2, 2)
>>> cart.get_total_items()
3
>>> cart.get_total_cost()
1200
>>> cart.remove_item(item1)
>>> cart.get_total_items()
2
>>> cart.get_total_cost()
200
"""

