list = [0, 1, 2, 0, 3]

i = 0

while (i < len(list)):
    if list[i] == 0:
        list.pop(i)
    else:
        i += 1

print(list)
