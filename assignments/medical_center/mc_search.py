from mc_data import patient_list

def search():
    search_term = str(input('Enter your search: '))
    search_result = []
    for i in patient_list:
        for key in i:
            if search_term == i[key]:
                search_result.append(i)
    return search_result