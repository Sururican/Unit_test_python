import unittest
from src.my_module import ShoppingCart, Item

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.item1 = Item('Laptop', 1000)
        self.item2 = Item('mause', 100)
        self.cart.add_item(self.item1)
        self.cart.add_item(self.item2, 2)

    def tearDown(self):
        ### 
        pass  
    def test_add_item(self):
        self.assertEqual(self.cart.get_total_items(), 3)

    def test_remove_item(self):
        self.cart.remove_item(self.item1)
        self.assertEqual(self.cart.get_total_items(), 2)

    def test_total_cost(self):
        self.assertEqual(self.cart.get_total_cost(), 1200)
        
    def test_item_type(self):
        self.assertTrue(isinstance(self.item1.name, str))
        self.assertTrue(isinstance(self.item1.price, (int, float)))
        self.assertTrue(isinstance(self.item2.name, str))
        self.assertTrue(isinstance(self.item2.price, (int, float)))

if __name__ == '__main__':
    unittest.main()