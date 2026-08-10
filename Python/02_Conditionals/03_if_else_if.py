size = input("Enter the order size (Small/Medium/Large): ")

if size == "small":
    print("Cost for the coffee is Rs. 10")
    # else if is written as elif
elif size == "medium":
    print("Cost for the coffee is Rs. 15")
elif size == "large":
    print("Cost for the coffee is Rs. 20")
else:
    print("Unknown cup size")
