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
    '''
    Gives user option to end or continue program
    '''
    cont = input('Would you like to do anything else? (Y/N) ')
    if cont == 'Y':
        run()
    else:
        print('Have a great day!!')
        fv.close()

def generate():
    '''
    creates list of restaurant objects
    use: res_list = generate()
    '''
    line = fv.readline()
    res_list = []
    while line != '':
        attributes = line.split('|')
        res_list.append(Restaurant(attributes[0], attributes[1],
                                    attributes[2], attributes[3], attributes[4]))
        line = fv.readline()
    return res_list

def create_menu():
    '''
    lets user add a restaurant to the restaurant file
    '''
    create_restaurant()
    end()


def run():
    '''
    Lets user run the program
    '''   
    print('What would you like to do?')
    for i, opt in enumerate(OPTIONS):
        print(f'{i}: {opt}')
    result = int(input('option: '))
    print()
    # brings up restaurant creation menu
    if result == 0:
        create_menu()
    # asks user to search for restaurant by name
    if result == 1:
        option1()
    # Brings up all restaurants matching user filter
    elif result == 2:
        print('What criterion would you like to filter by? ')
    # brings up a random restaurant matching user filter
    elif result == 3:
        option3()

def option1():
    '''
    Searches for restaurant for user
    '''
    name = input('Name: ')
    print()
    found = False
    # iterates through list of restaurants until a name match is found
    for i in res_list:
        if i.name() == name:
            print(i)
            found = True
            break
        if found is False:
            add = input('''no such restaurant exists.
Would you like to add it?(Y/N) ''')
            if add == 'Y':
                create_menu()
            else:
                end()
        else:
            end()

def option2():
    '''
    Brings up restaurants matching user's criteria
    '''
    for i, crit in enumerate(CRITERIA):
        print(f'{i}: {crit}')
    # ask user what to filter by
    criterion = int(input('Option: '))
    assert criterion in range(0,4)
    # ask user what to filter by
    filt = input('Filter by: ')
    # initialize found variable
    found = False
    for i in res_list:
        if i == filt:
            found = True
            print(i)
    # lets user create restaurant if desired one doesn't exist
    if found is False:
        add = input('''no such restaurant exists.
Would you like to add it?(Y/N) ''')
        if add == 'Y':
            create_menu()
        else:
            end()
    else:
        end()


def option3():
    '''
    Brings up random restaurant matching user filter
    '''
    print('What criterion would you like to filter by? ')
    for i, crit in enumerate(CRITERIA):
        print(f'{i+1}: {crit}')
    criterion = int(input('Option: '))
    assert criterion < 4, 'Not an option'
    filt = input('Criteria: ')
    matches = []
    found = False
    for i in res_list:
        if i == filt:
            found = True
            print(i)
    if found is False:
        add = input('''no such restaurant exists.
Would you like to add it?(Y/N) ''')
        if add == 'Y':
            create_menu()
        else:
            end()
    else:
        end()

res_list = generate()
run()
fv.close()
