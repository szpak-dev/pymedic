import json

from mc_generate_id import generate_id
from mc_view import ask, new_to_old, old_to_new, is_optional, validate, _labels


class Patient:
    first_name: str
    last_name: str
    dob: str
    gender: str
    phone: str
    email: str
    insurance: bool
    id: int

    def __init__(self, first_name: str, last_name: str, dob: str, gender: str, phone: str, email: str, insurance: bool, id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.gender = gender
        self.phone = phone
        self.email = email
        self.insurance = insurance
        self.id = id
    
    @classmethod
    def create_new_patient(cls):
        new_patient = {}
        for parameter, label in _labels.items():
            while True:
                value = input(f'{label}: ')

                if not value:
                    if is_optional(parameter):
                        break
                    else:
                        print('Field can not be empty. Try again.')
                        continue

                if is_bool(parameter):
                    value = _bool_map.get(value, None)
                

                try:
                    validate(parameter, value)
                except AssertionError as e:
                    print(str(e))
                    continue

            
                if value is not None:
                    new_patient[parameter] = value
                    break

            new_patient['id'] = generate_id()

        return cls(**new_patient)

            

_bool_map = {
    'yes': True, 'true': True, 'y': True, 't': True, 'on': True,
    'no': False, 'false': False, 'n': False, 'f': False, '': False
}

_bools = ['insurance']

with open('json.json', 'r') as file:
    patient_list = json.load(file)


def validate_form(form_data):
    # Empty Errors Dictionary
    form_errors = {}

    # Loop is checking and convering to bools
    for key, value in form_data.items():
        if is_bool(key):
            form_data[key] = _bool_map.get(value, None)

    #Loop validates and fills Errors Dictionary 
    for key, value in form_data.items():
        if not value:
            if is_optional(key): continue

            else:
                form_errors[key] = 'Field can not be empty'
        else:
            try:
                validate(key, value)
            except AssertionError as e:
                form_errors[key] = str(e)
    return form_errors



def is_bool(key):
    return key in _bools

def write_json(lista):
    with open('json.json', 'r+') as file:
        file.seek(0)
        json.dump(lista, file, indent=2)
        file.truncate()
   

    # transaltion between new and old keys            
    old_patient = {}
    for new_key in new_patient_dict:
        old_key = new_to_old(new_key)
        old_patient[old_key] = new_patient_dict[new_key]

    new_patient_dict = old_patient
    

    if is_new_patient_unique(new_patient_dict):
        persist_patient(new_patient_dict)
    else:
        print('Can not add duplicated patient to the database.')


def persist_patient(new_patient_dict: dict):
    patient_list.append(new_patient_dict)
    write_json(patient_list)
    print('Patient successfully added to the list.')


def is_new_patient_unique(new_patient_dict: dict):
    for i in patient_list:
        if new_patient_dict['First Name'] == i['First Name'] and new_patient_dict['Last Name'] == i['Last Name'] and new_patient_dict['Date of Birth (YYYY-MM-DD)'] == i['Date of Birth (YYYY-MM-DD)']:
            return False
        else:
            return True


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