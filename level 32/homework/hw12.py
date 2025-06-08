def find_longest_word(words):
    if not words:
        return None

    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

words_list = ["apple", "banana", "cherry", "blueberry"]
print(find_longest_word(words_list))
