import json
from mc_generate_id import generate_id

with open('json.json', 'r') as file:
    patient_list = json.load(file)

def write_json(lista):
    with open('json.json', 'r+') as file:
            file.seek(0)
            json.dump(lista, file, indent=2)
            file.truncate()

def register_new_patient():

    new_patient_dict = {'First Name': '', 'Last Name': '', 'Date of Birth (YYYY-MM-DD)': '', 'Gender (M/F/Other)': '', 'Phone Number': '', 'Email (optional)': '', 'Insurance (yes/no)': ''}
    for key in new_patient_dict:
        
        while True:
            value = input('Podaj - ' + key +': ')

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
            if new_patient_dict['First Name'] == i['First Name'] and new_patient_dict['Last Name'] == i['Last Name'] and new_patient_dict['Date of Birth (YYYY-MM-DD)'] == i['Date of Birth (YYYY-MM-DD)']:
                is_duplicated = True
            else:
                is_duplicated = False

    if not is_duplicated:
        patient_list.append(new_patient_dict)
        write_json(patient_list)
        print('Patient successfully added to the list.')
    else:
        print('Can not add duplicated patient to the database.')

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