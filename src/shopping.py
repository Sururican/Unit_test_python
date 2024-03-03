class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] -= quantity
            if self.items[item] <= 0:
                del self.items[item]
        else:
            raise ValueError("The item you want to remove is not available in the cart.")

    def get_total_cost(self):
        total_cost = 0
        for item, quantity in self.items.items():
            total_cost += item.price * quantity
        return total_cost

    def get_total_items(self):
        return sum(self.items.values())


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price