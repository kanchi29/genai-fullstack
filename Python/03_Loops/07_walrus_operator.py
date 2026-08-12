# Walrus operator (:=) allows you to assign a value to a variable as part of an expression
# This way the assigned value can be used immediately in a condition or other expression.

if (i := int(input("Enter your age: "))) > 18:  
    print("YAY! You can enter the pub!")
else:
    print("NO! You cannot enter the pub!")

