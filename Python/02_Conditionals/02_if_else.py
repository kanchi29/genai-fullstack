snack = input("Enter your preferred Snack: ")

print(f"Customer's choice: {snack}")

if snack == "Cookie" or snack == "Samosa":
    print("Order Confirmed! We will serve you shortly.")
else:
    print("Sorry, we only serve Cookie or Samosa")