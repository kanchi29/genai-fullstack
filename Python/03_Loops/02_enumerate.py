# enumerate() is a function that lets you loop through a sequence while getting both the index and the value

characters = ["John", "Finch", "Carter"]

for idx, item in enumerate(characters, start=1):  # isx is index 
    print(f"Character {idx}: {item}")

for pair in enumerate(characters):
    print(pair)

character_list = list(enumerate(characters))
print(character_list)

print(enumerate(characters))

# They're not lists. 
# They're iterators, meaning they generate their values as you loop over them rather than storing the whole result immediately.

# The key difference between zip and enumerate is where the values come from: 
# enumerate() automatically generates the index, while zip() takes corresponding values from multiple iterables.