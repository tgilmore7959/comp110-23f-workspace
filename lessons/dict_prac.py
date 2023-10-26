"""Practice with Dictoraries."""

# Constructing a dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Made my dictionary")
print(ice_cream)
# Adding a flavor
ice_cream["mint"] = 3
print(ice_cream)
# Add three orders of chocolate
ice_cream["chocolate"] += 3
print(ice_cream)
# Remove flavor
ice_cream.pop("mint")
print(ice_cream)

# Accessing a value
print(f"There are {ice_cream['chocolate']} orders of chocolate")
print(len(ice_cream))
if "mint" in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint")
else:
    print("no orders of mint")

for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders")

