# მომხმარებელს შემოატანინეთ ქულა
score = int(input("enter your score: "))

# შეფასება ქულის მიხედვით
if score > 80:
    grade = "A"
elif score > 60:
    grade = "B"
elif score > 40:
    grade = "C"
elif score > 20:
    grade = "D"
else:
    grade = "F"

    

# ვბეჭდავთ შეფასებას
print("your grade is:", grade)
