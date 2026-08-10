# Tuples are immutable, cannot be modified after creation
# Tuples are defined using parentheses () and can contain elements of different data types.

characters = ("Harry", "John", "Fusco", "Carter")

# let'say we want to allocate elements of tuple to variables:
# we will make another tuple of variables (same length as og tuple)

(char1, char2, char3, char4) = characters
print(f"Main Characters: {char1}, {char2}, {char3} and {char4}")

screen_time, character_time = 2, 1 
# we could use parathesis () here but it is not necessary
# python will automatically create a tuple of the values on the RHS and unpack them into the variables on the LHS

# basically python will automatically allocate the values 2 and 1 to the variables screen_time and character_time respectively
print(f"Screen Time: {screen_time}, Character Time: {character_time}")

# now if we had to reverse it, we can do it like this:
character_time, screen_time = screen_time, character_time
print(f"Screen Time: {screen_time}, Character Time: {character_time}")

# We can easily swap variables like this without any temp variable.

# Membership Test: We can check if an element is present in a tuple using the 'in' keyword.

print(f"Is Harry in characters? {'Harry' in characters}")

print(f"Is Zoe in characters? {'Zoe' in characters}")

