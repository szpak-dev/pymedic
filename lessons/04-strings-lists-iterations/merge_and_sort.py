list_a = [4, 1, 7]  
list_b = [3, 6, 2]

list_a.extend(list_b)

list_sorted = []

print(list_a)

for element in list_a:
    if element >= list_sorted[element + 1]:
        list_sorted.append(element)
    else:
        list_sorted.inset[0, element]
