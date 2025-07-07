list = [1, 3, 2, 3, 1, 4]
no_duplicates = []

list_len = len(list)
for element in range(list_len):
    if list[element] not in no_duplicates:
        no_duplicates.append(list[element])

print(no_duplicates)
