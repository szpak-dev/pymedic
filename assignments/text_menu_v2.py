
def main1():
    pass

menus = {
    'main_menu': {
        'title': '=== Medical Center ===',
        'options': {
            1: ('Patient list', patient_list_menu),
            2: ('Register new patient', main1),
            3: ('Exit', exit),
        }
    },
    'patient_list_menu': {
        'title': '=== Medical Center - Patient list ===',
        'options': {
            1: ('Show all', main1),
            2: ('Search for patient', main1),
            3: ('Filter Patients', main1),
            4: ('Back', exit),
        }
    }


}

def display_menu(menu_type):
    menu = menus[menu_type]
    for key, (name, _) in menu['options'].items():
        print(f'{key}: {name}')

def run_menu(menu_type):
    while True:
        display_menu(menu_type)

        choice = int(input('Enter your choice: '))
        menu = menus[menu_type]
        name, action = menu['options'][choice]
        action()



run_menu('main_menu')