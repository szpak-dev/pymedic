word = "Hello123!"

# nie można iterować po int
for letter in range(len(word)):
    char = word[letter]
    print(f"{char} > {ord(char)} > '{chr(ord(char) + 1)}' > {ord(char) + 1} ")