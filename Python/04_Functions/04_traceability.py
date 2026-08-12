# Excercise: Calculate final bill with GST for 3 orders

def add_gst(price, gst_rate):
    new_price = price + (price * gst_rate/100)
    return new_price

orders = [150, 220, 100]

for order in orders:
    final_bill = add_gst(order, 10)
    print(f"The final bill is: {final_bill}")

# Traceability of functions means being able to easily to trace errors or any other thing