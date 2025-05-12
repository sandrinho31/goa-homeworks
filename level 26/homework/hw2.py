
basket = ["apple", "banana", "orange", "grape", "mango"]

favorite_fruit = input("Enter your favorite fruit: ")


fruit_in_basket = False


for fruit in basket:
    if fruit == favorite_fruit:
        fruit_in_basket = True
        break


if fruit_in_basket:
    print("Good choice")
else:
    print("Fruit not in basket")