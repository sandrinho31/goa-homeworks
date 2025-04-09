pin = "3110"
tries = 0


user = input("enter pin: ")
while  user != pin :
    tries += 1
    print("wrong")
    user = input("enter pin: ")
print("correct")

print("you needed", tries , "tries")