# User has 3 attempts to enter the correct PIN
correct_pin = "1234"  # Replace with the desired correct PIN
attempts = 3

while attempts > 0:
    entered_pin = input("Enter your PIN: ")
    if entered_pin == correct_pin:
        print("Access Granted")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect PIN. You have {attempts} attempts left.")
        else:
            print("Access Denied")