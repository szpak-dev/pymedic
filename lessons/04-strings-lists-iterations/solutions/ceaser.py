program_action = input("Encrypt E or decrypt D?: ")

if program_action.lower() == "e":
    string = input("Enter your message: ")

    new_string = ""

    for char in string:
        if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
            letter_code = ord(char) + 3
            if (letter_code > 90 and letter_code <= 93) or (letter_code > 122 and letter_code <= 125):
                letter_code = letter_code - 26
                
        else:
            letter_code = ord(char)

        new_string = new_string + chr(letter_code)

    print(new_string) 
elif program_action.lower() == "d":

    string = input("Enter your message: ")

    new_string = ""

    for char in string:
        if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
            letter_code = ord(char) - 3
            if (letter_code < 65 and letter_code >= 62) or (letter_code < 97 and letter_code >= 94):
                letter_code = letter_code + 26
                
        else:
            letter_code = ord(char)

        new_string = new_string + chr(letter_code)

    print(new_string)
else:
    print("Type E to encrypt or D to decrypt.")



