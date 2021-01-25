pin_code = "6578"
entry_pin = input("Please provide a PIN number:\n")
while entry_pin != pin_code:
    print("Wrong PIN code, acces denied.\n")
    entry_pin = input("Please provide a PIN number:\n")
print("OK!")