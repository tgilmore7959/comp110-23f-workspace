"""Instantiating A Class."""


from lessons.classes.pizza import Pizza


my_pizza: Pizza = Pizza("large", 10, True)  # Constructor
# my_pizza.size = "large"
# my_pizza.toppings = 42
# my_pizza.gluten_free = False

# printing out some values
print(my_pizza)