import json

from mc_data import patient_list

from mc_generate_id import generate_id
from mc_patient_list_menu import patient_list_menu
from mc_new_patient import register_new_patient
from mc_search import search
from mc_delete import delete_patient

                
while True:
    print('=== Medical Center ===')
    print('1. Patient list')
    print('2. Register new patient')
    print('3. Make an appointment')
    print('4. Exit')

    choice_main = input('Enter your choice: ')

    if choice_main == '1': patient_list_menu()
    if choice_main == '2': register_new_patient()
    if choice_main == '3': continue
    if choice_main == '4': break

    