seat_type = input("Enter seat type(Sleeper/AC/General/Luxury): ").lower()

match seat_type:
    case "sleeper":
        print("No AC but bed is reserved")
    case "general":
        print("No AC and no reservation")
    case "ac":
        print("AC and bed is reserved")
    case "luxury":
        print("Premium seats with meals")
    case _:
        print("Invalid seat type")