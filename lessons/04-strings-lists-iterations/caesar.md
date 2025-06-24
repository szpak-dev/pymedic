# Caesar Cipher Encoder & Decoder Homework

## Introduction

The **Caesar cipher** is a classic encryption technique where each letter in a message is "shifted" by a fixed number of positions in the alphabet.

For example, using a **shift of 3**:

* `'A'` becomes `'D'`
* `'B'` becomes `'E'`
* `'X'` becomes `'A'`

This cipher is **simple, easy to break**, but great for learning about strings, characters, and ASCII values in Python.


## Your Task

Write a Python program that can:

1. **Encrypt** (cipher) a message using Caesar's shift
2. **Decrypt** (decipher) a message using the same shift
3. Handle both **uppercase and lowercase** letters correctly
4. Ignore non-alphabetic characters (they should stay unchanged)


## Hints

* Use `ord(char)` and `chr(number)` to convert between letters and their ASCII codes.
* Wrap letters around the alphabet using modulo arithmetic.
* Preserve spaces, punctuation, and numbers unchanged.


## Example

With **shift = 3**:

```text
Original : Hello, World!
Encrypted: Khoor, Zruog!
Decrypted: Hello, World!
```

## Requirements

* Define a function `encrypt(message: str, shift: int) -> str`
* Define a function `decrypt(message: str, shift: int) -> str`
* Use a simple main program to test both with user input or hardcoded values


## Bonus Challenge (Optional)

* Let the user choose whether to **encrypt or decrypt**
* Support both positive and negative shifts
* Add type hints to all functions


## Checklist

* The code runs without errors
* Encryption and decryption are correct for various messages and shift values
* Code is readable and well-structured
* You understand how `ord()` and `chr()` were used
