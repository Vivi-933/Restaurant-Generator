# Imports
from Restaurant_create import create_restaurant
from Restaurant import Restaurant
from random import randint

# Files
fv = open('restaurants.txt', 'r', encoding = 'utf-8')

# Constants
OPTIONS = ['create restaurant', 'view restaurant',
            'find restaurant(all)', 'find restaurant(random)']
CRITERIA = ['price', 'vegan', 'origin', 'type']


def end():
    cont = input('Would you like to do anything else? (Y/N) ')
    if cont == 'Y':
        run()
    else:
        print('Have a great day!!')
        fv.close()
    return

def generate():
    # creates list of restaurant objects
    line = fv.readline()
    res_list = []
    while line != '':
        attributes = line.split('|')
        res_list.append(Restaurant(attributes[0], attributes[1],
                                    attributes[2], attributes[3], attributes[4]))
        line = fv.readline()
    return res_list

def create_menu():
    create_restaurant()
    end()
    return

def run():    
    print('What would you like to do?')
    for i, opt in enumerate(OPTIONS):
        print(f'{i}: {opt}')
    result = int(input('option: '))
    print()

    # brings up restaurant creation menu
    if result == 0:
        create_menu()

    # asks user to search for restaurant by name
    elif result == 1:
        name = input('Name: ')
        print()
        line = fv.readline()
        found = False
        for i in res_list:
            if i.name() == name:
                print(i)
                break
            if found is False:
                add = input('''no such restaurant exists.
Would you like to add it?(Y/N) ''')
                if add == 'Y':
                    create_menu()
                else:
                    end()

    elif result == 2:
        print('What criterion would you like to filter by? ')

        # prints options menu
        for i, crit in enumerate(CRITERIA):
            print(f'{i+1}: {crit}')
        # ask user what to filter by    
        criterion = int(input('Option: '))
        assert criterion < 5, 'Not an option'
        filt = input('Filter by: ')
        # initialize found variable
        found = False

    elif result == 3:
        print('What criterion would you like to filter by? ')
        for i, crit in enumerate(CRITERIA):
            print(f'{i+1}: {crit}')
        criterion = int(input('Option: '))
        assert criterion < 4, 'Not an option'
        filt = input('Criteria: ')


res_list = generate()
run()
fv.close()
