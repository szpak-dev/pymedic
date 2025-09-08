menu_lvl = 1
import sys

menus = {
    'menu_st_1': {
        'f_menu': 'Main Menu 1',
        'main2': 'Main Menu 2',
        'main3': 'Main Menu 3',
        'exit': 'Main Menu 4'
    },
    'menu_st_2': {
        'f_menu': 'Sub Menu 1',
        'sub2': 'Sub Menu 2',
        'sub3': 'Sub Menu 3',
        'sub4': 'Sub Menu 4',
        'sub5': 'Sub Menu 5',
    },
    'menu_st_3': {
        'f_menu': 'Sub sub Menu 1',
        'sub2': 'Sub sub Menu 2',
        'sub3': 'Sub sub Menu 3',
        'sub4': 'Sub sub Menu 4',
        'sub5': 'Sub sub Menu 5',
    }
}

def f_menu():
    global menu_lvl
    menu_name = f'menu_st_{menu_lvl}'
    current_menu = menus[menu_name]
    for indeks, value in enumerate(current_menu.values()):
        print(f'{indeks + 1}: {value}')

    choice = int(input('Enter your choice: ')) - 1
    function_name = list(current_menu.keys())[choice]
    
    
    menu_lvl += 1
    globals()[function_name]()
    


f_menu()


#choice = input('Enter your choice: ')
#while True:
#    if choice = 