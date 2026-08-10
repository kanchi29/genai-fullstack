device_status = input("What is the status of the thermostat? ")

if device_status == "active":
    temp = int(input("Enter current temperature: "))    #input always returns a string so we do type conversion here
    if temp > 35:
        print("High Temperature Alert!")
    else:
        print("Temperature normal")
else:
    print("Device is off")