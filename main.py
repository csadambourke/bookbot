def word_count(file):
    words = file.split()
    return len(words)

def letter_count(file):
    letter_count = {}
    for l in file.lower():
        if l not in letter_count:
            letter_count[l] = 0
        letter_count[l] += 1
    return letter_count

file_name = "books/frankenstein.txt"

with open(file_name) as f:
    file_contents = f.read()
    num_of_words = word_count(file_contents)
    num_of_letters = letter_count(file_contents)
    print(f"--- Begin report of {file_name} ---")
    print(f"{num_of_words} were found in the document\n")
    letter_list = list(num_of_letters.keys())
    letter_list.sort()
    for l in letter_list:
        if l.isalpha():
            print(f"The '{l}' characters was found {num_of_letters[l]} times")
    print("--- End report ---")
