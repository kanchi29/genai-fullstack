footballer = "David Beckham"
print("Favourite footballer: ", footballer) 
def ted_lasso():
    def rebecca():
        global footballer # we are accessing global footballer in inner function
        footballer = "Jamie" # Inner Function - We overrode "David Beckham" and now it will be "Jamie" both in inner function and global scope
        print("Favourite footballer: ", footballer) 
    rebecca()

ted_lasso()
print("Favourite footballer: ", footballer) 