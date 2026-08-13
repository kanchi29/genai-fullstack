# def function_name(parameters) - Defining a function takes parameters
# function_name(arguements) - Calling a function takes arguments
# Depends on the argument's sequence type(datatype) and operation being performed if the original value of the argument gets changed or not

cups = [2, 4, 6]

def display_cups(quantity):
    print(quantity) # Prints the cups as it is

display_cups(cups)

def change_cups(quantity):
    quantity[1] = 8
    print(quantity) # Prints the new value of cups - mutable list

change_cups(cups)

# If the sequence type is immutable, then the reference of value would have to be changed.

# Two Types of Arguments - args & *kwargs

def colour(sun, leaf, wood):
    print(sun, leaf, wood)

colour("yellow", "green", "brown") # positional - automatically assigned to parameters based on position of arguments

colour(leaf="dark green", wood="deep brown", sun="neon yellow") #assigned to parameters based on keywords

# Now a mix of both:

def recipe(*ingredients, **extras):
    print("Main ingredients are:", ingredients)
    print("Extra ingredients are:", extras)

recipe("Sesame", "chickpeas", "olive oil", seasoning="basil", salad="caeser")

# So the "Sesame", "chickpeas", "olive oil" are expected arguements that will go in parameter with single asterick
# And the seasoning="basil", salad="caeser" are extra arguments that we can keep adding even later without worrying about number of variables to store them
# these extra arguments go into the parameter with double asterick **

# We can also assign values to parameters directly inthe function definition:
def game(name="GTA LV"):
    print(name)
game()
# If we want to initiate as an empty sequence we can do like:
def series(seasons = []): # OR def series(seasons = None): 
    print(seasons)

series()