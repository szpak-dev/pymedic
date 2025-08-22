from mc_data import patient_list
from mc_search import search
from mc_table import make_table
from mc_delete_patient import delete_patient

def patient_list_menu():
    while True:
        print('=== Medical Center -> Patients list ===')
        print('1. Show all')
        print('2. Search for patient')
        print('3. Filter patients')
        print('4. Update patient record')
        print('5. Export list to CSV')
        print('7. Back')

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


                            if choice_action == '2': 
                                delete_patient(search_results[patient_index]['id'])
                                break
                            if choice_action == '3': break

                            
                    if choice_search == '2': break
            elif len(search_results) == 0:
                break
            else:

                while True:
                            print('1. Edit patient data')
                            print('2. Delete patient')
                            print('3. Back')
                            choice_action = input('What would you like to do?:')


                            if choice_action == '2': 
                                delete_patient(search_results[0]['id'])
                                break
                            if choice_action == '3': break

        if choice_list == '7': break