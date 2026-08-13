# simple return:

def sales_report():
    return "100 toys sold today"

# print(f"Sales report says that: {sales_report()}")

# OR we could've stored the return value in a avriable first and then printed it:
report_result = sales_report()
print(f"Sales report says that: {report_result}")

# In some cases we have to early return from a function based on some condition:

def order(toys_left):
    if toys_left == 0:
        return("Sorry! No toys left for today.") # In case of early return, the rest of the code is not run and compiler moves out of the entire function
    return ("Here's your toy!")

print(order(3))
print(order(0))

# Multiple Returns Values: There can be only one valid return statement but more than one values being returned at once

def multiples(num):
    x = num * 1
    y = num * 2
    z = num * 3

    return x, y, z

# Now there should be equal number of variables ready to store these returned values:

a, b, c = multiples(5)
print (a, b, c)
abc = list(multiples(10)) # Another way is to store them in a list format
print (abc)