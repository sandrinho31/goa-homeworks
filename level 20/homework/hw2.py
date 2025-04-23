total = 0

while True:
    number = int(input("Enter a number: "))
    if number < 0:
        break
    total += number

print("Sum of positive numbers:", total)