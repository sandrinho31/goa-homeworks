start = int(input("შეიყვანეთ დაწყების რიცხვი: "))
end = int(input("შეიყვანეთ დასრულების რიცხვი: "))

if end < start:
    print("არასწორი შუალედი")
else:
    total = 0
    print("რიცხვები მოცემულ შუალედში:")
    for number in range(start, end + 1):
        print(number)
        total += number
    print(f"რიცხვების ჯამი: {total}")