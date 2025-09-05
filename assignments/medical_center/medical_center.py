import json

from mc_data import Patient, patient_list

from mc_patient_list_menu import patient_list_menu

                
while True:
    print('=== Medical Center ===')
    print('1. Patient list')
    print('2. Register new patient')
    print('3. Make an appointment')
    print('4. Exit')

    choice_main = input('Enter your choice: ')

    if choice_main == '1': patient_list_menu()
    if choice_main == '2': Patient.create_new_patient()
    if choice_main == '3': continue
    if choice_main == '4': break


    