def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

input_string = "Hello World"
print("Number of vowels:", count_vowels(input_string))