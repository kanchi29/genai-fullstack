order_cost = int(input("Enter the order amount: "))

delivery_fee = 0 if order_cost > 300 else 30

print(delivery_fee)

# Syntax for ternary operator:
# [value_if_true] if [condition] else [value_if_false]