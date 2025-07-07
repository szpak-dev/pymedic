list = [1, 3, 2, 3, 1, 4]
no_duplicates = []

for element in list:
    if element not in no_duplicates:
        calc = list.count(element)
        print(f"Number of {element}: {calc}")
        no_duplicates.append(element)


