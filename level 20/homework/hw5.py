numbers = []
while True:
    try:
        num = float(input("შეიყვანეთ რიცხვი (-1-ს შეყვანა შეწყვეტს): "))
        if num == -1:
            break
        elif num < -1:
            print("გთხოვთ, შეიყვანეთ -1 ან მეტი რიცხვი.")
        else:
            numbers.append(num)
    except ValueError:
        print("გთხოვთ, შეიყვანეთ ვალიდური რიცხვი.")

if numbers:
    average = sum(numbers) / len(numbers)
    print(f"შეყვანილი რიცხვების საშუალო არის: {average}")
else:
    print("არანაირი რიცხვი არ შეყვანილა.")