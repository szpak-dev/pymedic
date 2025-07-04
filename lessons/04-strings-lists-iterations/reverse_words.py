sentence = input("Type your expression: ")
new_sentence = ""




space_number = sentence.count(" ")
words = space_number


for word in range(words):
    space_index = sentence.find(" ")
    new_word = sentence[:space_index]
    new_word = new_word[::-1]
    new_sentence = new_sentence + " " + new_word
    sentence = sentence[space_index + 1:]
    word += 1

#problem z ostatnim słowem - nie kończy się zwykle spacją, dlatego ostatnie słowo poza pętlą
print(new_sentence + " " + sentence[::-1])


    



