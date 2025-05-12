
full_name = ""

result = ""


for i, char in enumerate(full_name):
    
    if (i == 0 or full_name[i - 1] == " ") and char.isupper():
       
        uppercase_letters = [c for c in full_name if c.isupper()]
        if len(uppercase_letters) >= 4:
           
            for letter in uppercase_letters[:4]:
                result += letter.lower()


print(result)