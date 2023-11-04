"""Defining a Class!"""

from __future__ import annotations


class Pizza:
    # attributes
    # Think of these as variables each instance of my class will have
    # <name> : <type>
    size: str
    toppings: int
    gluten_free: bool
    
    def __init__(self, inp_size: str, inp_toppings: int, inp_gf: bool):
        """My constructor."""
        self.size = inp_size
        self.toppings = inp_toppings
        self.gluten_free = inp_gf

    def price(self) -> float:
        """Calculate Pizza Price."""   
        price = float = 0.0
        if self.size == "large":
            price: float = 6.25
        else:
            price: float = 5.00
        price += .75 * self.toppings
        if self.gluten_free:
            price += 1.00
        return price
    
    def change_toppings(self, num_toppings: int) -> int:
        """Change number of toppings."""
        self.toppings += num_toppings

    def make_new_pizza_and_add_toppings(self, num_toppings: int) -> Pizza:
        """Make a new pizza with existing pizzas properties and add toppings."""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza
    