import math

string = "Never Odd Or Even"
new_string = string.replace(" ", "")
new_string = new_string.lower()
second_half_new_string = ""

string_len = len(new_string)
print(new_string)
print(string_len)

if string_len % string_len == 0:
    second_half_new_string = new_string[string_len/2:]
    if second_half_new_string[:-1] == new_string[0:string_len/2+1]:
        print("It's palindrome")
    else:
        print("It's not palindrome")
else:
    second_half_new_string = new_string[(string_len % 2)+1:]
    if second_half_new_string[:-1] == new_string[:math.ceil(string_len / 2)]:
        print("It's palindrome")
    else:
        print("It's not palindrome")