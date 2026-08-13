def characters():
    character = "John Reese"                       # Local Scope - Inside Function
    print(f"My favourite character is: {character}")

character = "Jocelyn Carter"                      # Global Scope - Outside Function
characters()
print(f"My favourite character is: {character}")

# Nested Functions Scope:

def ted_lasso():
    footballer = "Roy Kent" # Outer Function
    def rebecca():
        footballer = "Jamie" # Inner Function
        print("Favourite footballer: ", footballer) 
    rebecca()
    print("Favourite footballer: ", footballer) 

footballer = "Rajas" # Global Function
ted_lasso()
print("Favourite footballer: ", footballer) 