"""Instantiating A Class."""


from lessons.classes.pizza import Pizza


my_pizza: Pizza = Pizza("large", 10, True)  # Constructor
# my_pizza.size = "large"
# my_pizza.toppings = 42
# my_pizza.gluten_free = False

# printing out some values
# print("my_pizza: ")
# print(my_pizza)

# print("Pizza:")
# print(Pizza)

# print("Size Atribute:")
# print(my_pizza.size)
sals_pizza: Pizza = Pizza("medium", 5, False)


def price(input_pizza: Pizza) -> float:
    """Calculate Price of PIzza."""
    price: float = 0.0
    if input_pizza == "large":
        price: float = 6.25
    else:
        price: float = 5.00
    price += .75 * input_pizza.toppings
    if input_pizza.gluten_free:
        price += 1.00
    return price


print(price(sals_pizza))
print(price(my_pizza))

print(sals_pizza.price())
print(my_pizza.price())

my_pizza.change_toppings(2)
print(my_pizza.price())

my_other_pizza: Pizza = my_pizza.make_new_pizza_and_add_toppings(2)
print(my_other_pizza.toppings)