#An object can have a unqiue identity, a unique type and a value.
#Objects are either Mutable or Immutable - can be distinguished with the help of identity (not value)
#For mutable objects: there are two ways in which an object is mutable
# In the storage a number cannot be changed so if we're changing the value of an object from one number 
# to another, we are basically changing the reference of that object from one number to a different number, they both will have different
# id numbers but the original object remains same.
# Other way is for objects which can be changed in storage, example- a set can have values added or removed but its id number remains the same
# so the point of reference also remains same
# either ways, the object can be called mutable.

sugar_cubes = 2
print(f"Initial sugar quantity: {id(sugar_cubes)}")
sugar_cubes = 5
print(f"Updated sugar quantity: {id(sugar_cubes)}")

# output:
# Initial sugar quantity: 4303563088
# Updated sugar quantity: 4303563184
# reference of sugar_cubes has changed from 4303563088 to 4303563184, so the number itself didn't change but the reference of the object has changed, so it is mutable.

spices = {"salt", "pepper"}
print(f"Initial spices quantity: {id(spices)}")
spices.add("cinnamon")
print(f"Updated spices quantity: {id(spices)}")

# output:
# Initial spices quantity: 4299265856
# Updated spices quantity: 4299265856
# reference of spices has not changed, so the object itself has changed in storage but the reference of the object has not changed, so it is mutable. 