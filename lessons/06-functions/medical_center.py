patient_list = [{'First Name: ': 'John', 'Last Name: ': 'Doe', 'Date of Birth (YYYY-MM-DD): ': '1985-04-12', 'Gender (M/F/Other): ': 'M', 'Phone Number: ': '+48123456789', 'Email (optional): ': 'john.doe@example.com', 'Insurance (yes/no): ': 'yes', 'id': 'P00001'},
              {'First Name: ': 'Jon', 'Last Name: ': 'Doe', 'Date of Birth (YYYY-MM-DD): ': '1990-03-01', 'Gender (M/F/Other): ': 'M', 'Phone Number: ': '+48123456789', 'Email (optional): ': 'john.doe@example.com', 'Insurance (yes/no): ': 'no', 'id': 'P00002'}]


def patient_list_menu():
    while True:
        print('=== Medical Center -> Patients list ===')
        print('1. Show all')
        print('2. Search for patient')
        print('3. Filter patients')
        print('4. Update patient record')
        print('5. Export list to CSV')
        print('6. Delete patient')
        print('7. Back')

        choice_list = input('Enter your choice: ')

        if choice_list == '1': print(patient_list)
        if choice_list == '2': search()
        if choice_list == '7': break

def generate_id():
    with open('C:\\Users\\lumac\\Documents\\Python lekcje\\new.txt', 'r') as file:
        generated_id = file.read().strip()
        file.close()
    counter = int(generated_id) + 1
    with open('C:\\Users\\lumac\\Documents\\Python lekcje\\new.txt', 'w') as file:
        file.write(str(counter))
    return generated_id

def search():
    search_term = str(input('Enter your search: '))
    search_result = []
    for i in patient_list:
        for key in i:
            if search_term == i[key]:
                search_result.append(i)
    print(search_result)

def delete_patient ():
    pass

def register_new_patient():
    new_patient_dict = {'First Name: ': '', 'Last Name: ': '', 'Date of Birth (YYYY-MM-DD): ': '', 'Gender (M/F/Other): ': '', 'Phone Number: ': '', 'Email (optional): ': '', 'Insurance (yes/no): ': ''}
    for key in new_patient_dict:
        
        while True:
            value = input('Podaj - ' + key)

            if not value:
                if 'optional' in key.lower():
                    break
                else:
                    print('Field can not be empty. Try again.')
                    continue

            if 'email' in key.lower() and '@' not in value:
                print('Wrong email address. Try again.')
                continue
            if 'phone' in key.lower():
                value = value.strip()
                if value.isdigit() and len(value) == 9:
                    new_patient_dict[key] = value
                    break
                else:
                    print('Wrong phone number. Try again.')
                    continue
                
            if value:
                new_patient_dict[key] = value
                break
                
            
           

    new_patient_id = generate_id()
    new_patient_dict['id'] = new_patient_id

    is_duplicated = False

    for i in patient_list:
            if new_patient_dict['First Name: '] == i['First Name: '] and new_patient_dict['Last Name: '] == i['Last Name: '] and new_patient_dict['Date of Birth (YYYY-MM-DD): '] == i['Date of Birth (YYYY-MM-DD): ']:
                is_duplicated = True
            else:
                is_duplicated = False

    if not is_duplicated:
        patient_list.append(new_patient_dict)
        print('Patient successfully added to the list.')
    else:
        print('Patient duplicated')

                


    

while True:
    print('=== Medical Center ===')
    print('1. Patient list')
    print('2. Register new patient')
    print('3. Make an appointment')
    print('4. Exit')

    choice_main = input('Enter your choice: ')

    if choice_main == '1': patient_list_menu()
    if choice_main == '2': register_new_patient()
    if choice_main == '4': break