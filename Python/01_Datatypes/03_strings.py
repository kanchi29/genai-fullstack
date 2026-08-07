# Strings are immutable
# Declaration and Initialisation:
name = "John Reese"
profession = "Security Personnel"
name2 = "Harold Finch"
show = "Person of Interest"
print(f"{name} is a {profession} that works for {name2} in the TV Show {show}.")

# Indexing & Slicing:
# Indexing of strings starts from 0. 
# Last number (End) index of the string is NOT inclusive in indexing.
# Syntax is string_variable[start_index:end_index]

print(f"First name of the character is {name[0:4]}")
print(f"Last name of the character is {name[5:10]}")

# Now if we put a third number in the end index, it will act as an iterator and will skip the characters in between.
print(f"Even characters in the profession of the character are {profession[0:18:2]}")
# We can reverse a string by using negative indexing by putting sign in front of the iterator index.
print(f"Reversed name of the character is {name[::-1]}")
 # First word and Last word:
print(f"First word in the show name is {show[:6]}")
# We can skip writing the first index if we want to start from the beginning of the string.
print(f"Last word in the show name is {show[10:]}")
# We can skip writing the last index if we want to go till the end of the string.