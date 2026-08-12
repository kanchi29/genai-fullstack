def total_bill(total_cups, price_per_cup):
    return total_cups * price_per_cup

print(f"Order for table: {total_bill(3, 15)}")
print(f"Order for table: {total_bill(4, 25)}")
print(f"Order for table: {total_bill(1, 50)}")

# Functions improve readability by hiding the complex part