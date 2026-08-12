# zip() lets you combine elements from two or more sequences together, position by position.

# They're not lists. 
# They're iterators, meaning they generate their values as you loop over them rather than storing the whole result immediately.

# The key difference between zip and enumerate is where the values come from: 
# enumerate() automatically generates the index, while zip() takes corresponding values from multiple iterables.

characters = ["John", "Finch", "Fusco", "Carter"]
age = ["40", "42", "51", "41"]

# for age, characters in zip(age, characters):
#     print(f"{characters}'s age is {age}")

height = ["6'2", "5'11", "5'10", "5'9"]

for age, characters, height in zip(age, characters, height):
    print(f"{characters}'s age is {age} and height is {height}")