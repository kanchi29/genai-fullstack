# Syntax for range() sequence in for loops
# for [iterator_variable] in range([start], [end]):
# in the range, the 'end' is not inclusive

for token in range(1,5):
    print(f"Serving coffee to token #{token}")

#Syntax for looping through a list
# for iterator_variable] in [list_variable]:

orders = ['John', 'Finch', 'Fusco', 'Carter']
for name in orders:
    print(f"Order ready for {name}")