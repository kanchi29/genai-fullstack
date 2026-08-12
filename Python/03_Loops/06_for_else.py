staff = [("Kanchi", 24), ("Harsh", 15), ("Aditya", 26), ("Abhishek", 34),]

# for name, age in staff:
#     if age > 26:
#         print(f"{name} is Hired!!")
#         break
# else:
#     print("No one is Hired!")

# for name, age in staff:
#     if age > 35:
#         print(f"{name} is Hired!!")
#         break
# else:
#     print("No one is Hired!")

for name, age in staff:
    if age > 25:
        print(f"{name} is Hired!!")
        break
else:
    print("No one is Hired!")