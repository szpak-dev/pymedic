from mc_data import patient_list
from mc_table import make_table
from mc_data import delete_patient

def search():
    search_term = str(input('Enter your search: '))
    search_result = []
    for i in patient_list:
        for key in i:
            if search_term == i[key] and i not in search_result:
                search_result.append(i)
    return search_result

def patient_list_menu():
    while True:
        print('=== Medical Center -> Patients list ===')
        print('1. Show all')
        print('2. Search for patient')
        print('3. Filter patients')
        print('4. Back')

        choice_list = input('Enter your choice: ')

        if choice_list == '1': make_table(patient_list)
        if choice_list == '2': 
            search_results = search()
            make_table(search_results)
            if len(search_results) > 1:
                while True:
                    print('1. Select patient')
                    print('2. Go back')
                    choice_search = input('What would you like to do?: ')
                    if choice_search == '1': 
                        while True:
                            choice_patient = input('Which patient would you like to select? Enter ordinal number: ')
                            patient_index = int(choice_patient) - 1
                            print(search_results[patient_index]['id'])
                            break
                        while True:
                            print('1. Edit patient data')
                            print('2. Delete patient')
                            print('3. Back')
                            choice_action = input('What would you like to do?:')

                            if choice_action == '1':
                                 while True:
                                    print('1. First name')
                                    print('2. Last name')
                                    print('3. Date of birth')
                                    print('4. Gender')
                                    print('5. Phone number')
                                    print('6. Email')
                                    print('7. Insurance')
                                    print('8. Go back')
                                    choice_data_for_edit = input('Which data would you like to edit?: ')
                                    
                                    if choice_data_for_edit == '1':
                                        new_data = input('Enter updated first name: ')
                                        success = False
                                        for i in patient_list:
                                            if i['id'] == search_results[patient_index]['id']:
                                                i['First Name'] = new_data
                                                success = True
                                        if success: print('Patient data changed successfully.')

                                    if choice_data_for_edit == '2':
                                        new_data = input('Enter updated last name: ')
                                        success = False
                                        for i in patient_list:
                                            if i['id'] == search_results[patient_index]['id']:
                                                i['Last Name'] = new_data
                                                success = True
                                        if success: print('Patient data changed successfully.')

                                    if choice_data_for_edit == '3':
                                        new_data = input('Enter updated date of birth: ')
                                        success = False
                                        for i in patient_list:
                                            if i['id'] == search_results[patient_index]['id']:
                                                i['Date of Birth (YYYY-MM-DD)'] = new_data
                                                success = True
                                        if success: print('Patient data changed successfully.')

                                    if choice_data_for_edit == '4':
                                        new_data = input('Enter updated gender: ')
                                        success = False
                                        for i in patient_list:
                                            if i['id'] == search_results[patient_index]['id']:
                                                i['Gender (M/F/Other)'] = new_data
                                                success = True
                                        if success: print('Patient data changed successfully.')

                                    if choice_data_for_edit == '5':
                                        new_data = input('Enter updated phone number: ')
                                        success = False
                                        for i in patient_list:
                                            if i['id'] == search_results[patient_index]['id']:
                                                i['Phone Number'] = new_data
                                                success = True
                                        if success: print('Patient data changed successfully.')
                                    
                                    if choice_data_for_edit == '6':
                                        new_data = input('Enter updated email: ')
                                        success = False
                                        for i in patient_list:
                                            if i['id'] == search_results[patient_index]['id']:
                                                i['Email (optional)'] = new_data
                                                success = True
                                        if success: print('Patient data changed successfully.')

                                    if choice_data_for_edit == '7':
                                        new_data = input('Enter updated insurance status (yes/no): ')
                                        success = False
                                        for i in patient_list:
                                            if i['id'] == search_results[patient_index]['id']:
                                                i['Insurance (yes/no)'] = new_data
                                                success = True
                                        if success: print('Patient data changed successfully.')

                                    if choice_data_for_edit == '8': break

                            if choice_action == '2': 
                                delete_patient(search_results[patient_index]['id'])
                                break
                            if choice_action == '3': break

                            
                    if choice_search == '2': break
            elif len(search_results) == 0:
                print('Nothing found. Try again.')
                break
            else:
                patient_index = 0
                while True:
                            print('1. Edit patient data')
                            print('2. Delete patient')
                            print('3. Back')
                            choice_action = input('What would you like to do?:')

                            if choice_action == '1':
                                 while True:
                                    print('1. First name')
                                    print('2. Last name')
                                    print('3. Date of birth')
                                    print('4. Gender')
                                    print('5. Phone number')
                                    print('6. Email')
                                    print('7. Insurance')
                                    print('8. Go back')
                                    choice_data_for_edit = input('Which data would you like to edit?: ')

                                    if choice_data_for_edit == '1':
                                        new_data = input('Enter updated first name: ')
                                        success = False
                                        for i in patient_list:
                                            if i['id'] == search_results[patient_index]['id']:
                                                i['First Name'] = new_data
                                                success = True
                                        if success: print('Patient data changed successfully.')

                                    if choice_data_for_edit == '2':
                                        new_data = input('Enter updated last name: ')
                                        success = False
                                        for i in patient_list:
                                            if i['id'] == search_results[patient_index]['id']:
                                                i['Last Name'] = new_data
                                                success = True
                                        if success: print('Patient data changed successfully.')

                                    if choice_data_for_edit == '3':
                                        new_data = input('Enter updated date of birth: ')
                                        success = False
                                        for i in patient_list:
                                            if i['id'] == search_results[patient_index]['id']:
                                                i['Date of Birth (YYYY-MM-DD)'] = new_data
                                                success = True
                                        if success: print('Patient data changed successfully.')

                                    if choice_data_for_edit == '4':
                                        new_data = input('Enter updated gender: ')
                                        success = False
                                        for i in patient_list:
                                            if i['id'] == search_results[patient_index]['id']:
                                                i['Gender (M/F/Other)'] = new_data
                                                success = True
                                        if success: print('Patient data changed successfully.')

                                    if choice_data_for_edit == '5':
                                        new_data = input('Enter updated phone number: ')
                                        success = False
                                        for i in patient_list:
                                            if i['id'] == search_results[patient_index]['id']:
                                                i['Phone Number'] = new_data
                                                success = True
                                        if success: print('Patient data changed successfully.')
                                    
                                    if choice_data_for_edit == '6':
                                        new_data = input('Enter updated email: ')
                                        success = False
                                        for i in patient_list:
                                            if i['id'] == search_results[patient_index]['id']:
                                                i['Email (optional)'] = new_data
                                                success = True
                                        if success: print('Patient data changed successfully.')

                                    if choice_data_for_edit == '7':
                                        new_data = input('Enter updated insurance status (yes/no): ')
                                        success = False
                                        for i in patient_list:
                                            if i['id'] == search_results[patient_index]['id']:
                                                i['Insurance (yes/no)'] = new_data
                                                success = True
                                        if success: print('Patient data changed successfully.')

                                    if choice_data_for_edit == '8': break

                            if choice_action == '2': 
                                delete_patient(search_results[0]['id'])
                                break
                            if choice_action == '3': break

        if choice_list == '4': break