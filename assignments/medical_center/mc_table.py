import tabulate

def make_table(list_of_dictionaries):
    if list_of_dictionaries != []:
        rows = []
        for i in range(len(list_of_dictionaries)):
            row = [i + 1]
            row.extend(list_of_dictionaries[i].values())
            rows.append(row)
        header_with_number = ["Nr"]
        header_with_number.extend(list_of_dictionaries[0].keys())
        print(tabulate.tabulate(rows, header_with_number))
    else:
        print('Table empty. No patient in the database.')
