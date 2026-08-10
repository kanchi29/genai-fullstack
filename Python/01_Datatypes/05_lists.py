# Lists are mutable and are like arrays (arrays is not there in python).
# Lists can contain elements of different data types.
# There are many built-in methods that can be used to modify or work with lists.

characters = ['John', 'Finch', 'Fusco', 'Carter']
print(characters)

characters.append('Root')  # Adds an element to the end of the list
print(characters)

characters.remove('Fusco') # Removes an element from the list
print(characters)

characters.insert(2, 'Zoe') # With insert, we can add element at a specific index
print(characters)

# pop method removes the last element from the list and returns it
last_character = characters.pop()
print(last_character)

characters.reverse() # Reverses the order of the list
print(characters)

characters.sort() # Sorts the list in ascending order
print(characters)

# max(list) and min(list) can be used to find the maximum and minimum values in a list
