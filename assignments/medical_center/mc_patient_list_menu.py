from mc_data import patient_list
from mc_search import search
from mc_table import make_table

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

        if choice_list == '1': make_table(patient_list)
        if choice_list == '2': 
            make_table(search())
            while True:
                print('1. Update patient data')
                print('2. Make and appointment')
                print('3. Update patient data')
                print('4. Go back')
                choice_search = input('What would you like to do?: ')
                

                if choice_search == '4': break

        if choice_list == '7': break