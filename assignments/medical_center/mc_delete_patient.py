import json
from mc_data import patient_list

def delete_patient(id_for_deletion):
    
    success = False
    for i in patient_list:
        if i['id'] == id_for_deletion:
            patient_list.remove(i)
            with open('json.json', 'r+') as file:
                file.seek(0)
                json.dump(patient_list, file, indent=2)
                file.truncate()
                success = True
            
    if success:
        print(f'Patient {id_for_deletion} succesfully removed.')
    else:
        print(f'Patient {id_for_deletion} not found. Unable to delete.')