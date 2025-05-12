user_choice = input("enter a number from 0 to 4: ")
vegetables = ["carrot", "broccoli", "spinach", "potato", "tomato"]
if user_choice == "0":
    print(vegetables[0])
elif user_choice == "1":
    print(vegetables[1])    
elif user_choice == "2":
    print(vegetables[2])
elif user_choice == "3":
    print(vegetables[3])
elif user_choice == "4":
    print(vegetables[4])
else:
    print("Please enter a number from 0 to 4.")