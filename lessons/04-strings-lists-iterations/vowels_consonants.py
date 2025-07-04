string = "artificialintelligence"
new_string = ""

vowels = "aeiouy"

vowels_num = 0
letters = len(string)

for letter in range(letters):
    char = string[letter]
    if char not in new_string:
        new_string = new_string + char

letters = len(new_string)

for letter in range(letters):
    if new_string[letter] in vowels:
        vowels_num += 1
    letter += 1

print(f"Vowels: {vowels_num}")
print(f"Consonants: {letters-vowels_num}")

