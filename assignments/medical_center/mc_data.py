import json

from mc_generate_id import generate_id
from mc_view import ask, new_to_old, old_to_new, is_optional, validate


with open('json.json', 'r') as file:
    patient_list = json.load(file)


def write_json(lista):
    with open('json.json', 'r+') as file:
        file.seek(0)
        json.dump(lista, file, indent=2)
        file.truncate()


def register_new_patient():
    new_patient_dict = {'first_name': '', 'last_name': '', 'dob': '', 'gender': '', 'phone': '', 'email': '', 'insurance': ''}
    for key in new_patient_dict:

        while True:
            value = ask(key)
            validate(key, value)

            if not value:
                if is_optional(key):
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

    # transaltion between new and old keys            
    old_patient = {}
    for new_key in new_patient_dict:
        old_key = new_to_old(new_key)
        old_patient[old_key] = new_patient_dict[new_key]

    new_patient_dict = old_patient
    new_patient_id = generate_id()
    new_patient_dict['id'] = new_patient_id

    if is_new_patient_unique(new_patient_dict):
        persist_patient(new_patient_dict)
    else:
        print('Can not add duplicated patient to the database.')


def persist_patient(new_patient_dict: dict):
    patient_list.append(new_patient_dict)
    write_json(patient_list)
    print('Patient successfully added to the list.')


def is_new_patient_unique(new_patient_dict: dict):
    is_duplicated = False
    for i in patient_list:
        if new_patient_dict['First Name'] == i['First Name'] and new_patient_dict['Last Name'] == i['Last Name'] and new_patient_dict['Date of Birth (YYYY-MM-DD)'] == i['Date of Birth (YYYY-MM-DD)']:
            is_duplicated = True
        else:
            is_duplicated = False
    return is_duplicated


def delete_patient(id_for_deletion):
    success = False
    for i in patient_list:
        if i['id'] == id_for_deletion:
            patient_list.remove(i)
            write_json(patient_list)
            success = True
            
    if success:
        print(f'Patient {id_for_deletion} succesfully removed.')
    else:
        print(f'Patient {id_for_deletion} not found. Unable to delete.')