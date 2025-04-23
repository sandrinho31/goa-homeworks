# Prompt the user to enter a sentence
sentence = input("შეიყვანეთ წინადადება: ")

# Define vowels
vowels = "aeiouAEIOU"

# Initialize counters
vowel_count = 0
consonant_count = 0

# Iterate through each character in the sentence
for char in sentence:
    if char.isalpha():  
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Print the results
print(f"ხმოვნების რაოდენობა: {vowel_count}")
print(f"თანხმოვნების რაოდენობა: {consonant_count}")