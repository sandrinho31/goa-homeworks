# შექმენით სია 0-დან 15-მდე რიცხვებით
numbers = list(range(16))

# გამოიტანეთ მხოლოდ ის რიცხვები, რომლებიც კენტ ინდექსებზე დგანან
odd_index_numbers = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]

print(odd_index_numbers)