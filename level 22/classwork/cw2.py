
cold_drinks = ["Coca-Cola", "Pepsi", "Sprite", "Fanta", "Mountain Dew"]
favorite_drink = "Sprite"  


user_drink = input("შეიყვანეთ სასმელი: ")
if user_drink in cold_drinks:
    print("თქვენი სასმელი არის:", user_drink)
else:
    print("თქვენი სასმელი არ არის სიაში")

if user_drink == favorite_drink:
    print("თქვენი სასმელი არის ჩემი საყვარელი სასმელი")
else:
    print("თქვენი სასმელი არ არის ჩემი საყვარელი სასმელი")
