names_list = ['Anna', 'Tom', 'Anna', 'Eli', 'Tom', 'Eli', 'Anna']

name_dictionary: dict[str, int] = {}

for name in names_list:
    if name in name_dictionary:
        name_dictionary[name] += 1
    else:
        name_dictionary[name] = 1

print(name_dictionary)