# Making a variable non local means when we're accessing a variable in out function from the inner function,
# we need to extend the scope of the outer function variable to make it non locakl and be able to use in inner function
# Happens in cases of nested functions

def ted_lasso():
    footballer = "Roy Kent" # Outer Function
    def rebecca():
        nonlocal footballer # we made outer function footballer non local
        footballer = "Jamie" # Inner Function - We overrode "Roy Kent" and now it will be "Jamie" both in inner and outer function
        print("Favourite footballer: ", footballer) 
    rebecca()
    print("Favourite footballer: ", footballer) 

ted_lasso()