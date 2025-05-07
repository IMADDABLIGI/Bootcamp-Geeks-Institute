sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# print(sandwich_orders)

for order in sandwich_orders:
    if order == "Pastrami sandwich":
        sandwich_orders.remove(order)


finished_sandwiches = []

while len(sandwich_orders) > 0:
    pop_value = sandwich_orders.pop(0)
    finished_sandwiches.append(pop_value)

# i = 0
# for order in sandwich_orders:
#     finished_sandwiches.append(sandwich_orders.pop(i))
#     i += 1

for order in finished_sandwiches:
    print(f"I made your {order}")

# print(finished_sandwiches)