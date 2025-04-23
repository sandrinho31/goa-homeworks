even_count = 0
odd_count = 0

while True:
    try:
        number = int(input("შეიყვანეთ რიცხვი (უარყოფითი რიცხვი შეყვანის შესაწყვეტად): "))
        if number < 0:
            break
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    except ValueError:
        print("გთხოვთ შეიყვანოთ ვალიდური რიცხვი.")

print(f"ლუწი რიცხვების რაოდენობა: {even_count}")
print(f"კენტი რიცხვების რაოდენობა: {odd_count}")