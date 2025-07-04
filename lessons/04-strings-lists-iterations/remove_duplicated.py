string = "programming"
new_string = ""

letters = len(string)

for letter in range(letters):
    char = string[letter]
    if char not in new_string:
        new_string = new_string + char


print(new_string)