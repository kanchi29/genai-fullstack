# sets are mutable unordered collections of unique elements. Defined by curly braces {}
# They are useful for membership testing, removing duplicates from a sequence, and performing mathematical operations like union, intersection, difference, and symmetric difference.

Male_characters = {'John', 'Finch', 'Fusco', 'Bear'}
Female_characters = {'Carter', 'Root', 'Zoe', 'Bear'}

# Putting 'Bear' to have a commong element in both

Main_characters = Male_characters.union(Female_characters) # union() method returns a new set with all unique
print(Main_characters)

# Can also we written as:
# Main_characters = Male_characters | Female_characters

# To find intersection:
Neutral_characters = Male_characters & Female_characters
# Can also be written as Male_characters.intersection(Female_characters)
print(Neutral_characters)

strictly_males = Male_characters - Female_characters
print(strictly_males)
# Difference method, denoted by '-' gives elements strictly from one set, removing any common elements

# There is a Frozen set which is exactly like normal Sets but it is mutable.