patient_list = [{'First Name: ': 'John', 'Last Name: ': 'Doe', 'Date of Birth (YYYY-MM-DD): ': '1985-04-12', 'Gender (M/F/Other): ': 'M', 'Phone Number: ': '+48123456789', 'Email (optional): ': 'john.doe@example.com', 'Insurance (yes/no): ': 'yes', 'Patient registered with ID: ': 'P00001'},
              {'First Name: ': 'John', 'Last Name: ': 'Doe', 'Date of Birth (YYYY-MM-DD): ': '1985-104-12', 'Gender (M/F/Other): ': 'M', 'Phone Number: ': '+48123456789', 'Email (optional): ': 'john.doe@example.com', 'Insurance (yes/no): ': 'no', 'Patient registered with ID: ': 'P00002'}]

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
    pass

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
    new_patient_dict = {'First Name: ': '', 'Last Name: ': '', 'Date of Birth (YYYY-MM-DD): ': '', 'Gender (M/F/Other): ': '', 'Phone Number: ': '', 'Email (optional): ': '', 'Insurance (yes/no): ': '', 'Patient registered with ID: ': ''}
    for key in new_patient_dict:
        value = input('Podaj - ' + key)
        new_patient_dict[key] = value
    patient_list.append(new_patient_dict)
    print('Patient successfully added to the list.')

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