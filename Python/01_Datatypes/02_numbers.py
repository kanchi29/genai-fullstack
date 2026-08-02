# Numbers- Integers, Boolean, Real Numbers(Decimal Float), Complex Numbers(x + yi)
# Operations +, -, *, /, // (divide but return integer even if float), % (modulus- for remainder), ** (exponentiation)
# Boolean - True (1), False (0)
# Any number besides 0 is True, 0, None, [], {} are False 

milk_present = 1 # or any number can be used to represent True
print(f"Is there milk present? {bool(milk_present)}")  # True

milk_present = None # or any value that is considered False can be used to represent False
print(f"Is there milk present? {bool(milk_present)}")  # False

# the 'bool' function converts any value to a boolean value. In Python, the following values are considered False:
# None, False, 0 (zero), 0.0 (zero float), 0j (zero complex), '' (empty string) 

# Operations - AND, OR, NOT (written just as 'and', 'or', 'not')