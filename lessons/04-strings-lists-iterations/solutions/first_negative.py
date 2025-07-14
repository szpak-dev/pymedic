list = [3, 5, -2, 4]

i = 0

while i < len(list):
    if list[i] < 0:
        break
    i += 1

print(list[i])
