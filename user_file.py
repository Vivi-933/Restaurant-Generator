# Imports
from Restaurant_create import create_restaurant
from Restaurant import Restaurant
from random import randint

# Files
fv = open('restaurants.txt', 'r', encoding = 'utf-8')

# Constants
OPTIONS = ['create restaurant', 'view restaurant', 'find restaurant(all)', 'find restaurant(random)']
CRITERIA = ['price', 'vegan', 'origin', 'type']


def end():
        cont = input('Would you like to do anything else? (Y/N) ')
        if cont == 'Y':
                run()
        else:
                print('Have a great day!!')
        return

def create_menu():
        create_restaurant()
        end()
        return

def run():
    print('What would you like to do?')
    for i in range(len(OPTIONS)):
                print(i, OPTIONS[i])
    result = int(input('option: '))

    if result == 0:
            create_menu()

    elif result == 1:
            name = input('Name: ')
            line = fv.readline()
            found = False
            while line != '':
                    attributes = line.split(',')
                    line = fv.readline()
                    if attributes[0] == name:
                            line = ''
                            found = True
                            res = Restaurant(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4])
                            print(res)              
            if found is True:
                    print(res)

            else:
                    add = input('''no such restaurant exists.
                        Would you like to add it?(Y/N) ''')
                    if add == 'Y':
                            create_menu()
                    else:
                        end()
    elif result == 2:
            print('What criterion would you like to filter by? ')
            for i in range(len(CRITERIA)):
                print(i, CRITERIA[i])
            criterion = int(input('Option: '))
            assert criterion < 4, 'Not an option'
            filt = input('Criteria: ')
            if criterion != 3:
                line = fv.readline()
                while line != '':
                        attributes = line.split(',')
                        line = fv.readline()
                        if attributes[criterion] == filt:
                                found = True 
                                res = Restaurant(attributes)
                                print(res)
                if not found:
                    add = input('''no such restaurant exists.
                        Would you like to add it?(Y/N) ''')
                    if add == 'Y':
                            create_menu()
                    else:
                        end()
                        
    elif result == 3:
            print('What criterion would you like to filter by? ')
            for i in range(len(CRITERIA)):
                print(i, CRITERIA[i])
            criterion = int(input('Option: '))
            assert criterion < 4, 'Not an option'
            filt = input('Criteria: ')
            restaurants = []
            if criterion != 3:
                line = fv.readline()
                while line != '':
                        attributes = line.split(',')
                        line = fv.readline()
                        if attributes[criterion] == filt:
                                found = True 
                                res = Restaurant(attributes)
                                restaurants.append(res)
                if not found:
                        add = input('''no such restaurant exists.
                            Would you like to add it?(Y/N) ''')
                        if add == 'Y':
                                create_menu()
                        else:
                            end()
                else:
                       rand = randint(0,len(restaurants)-1)
                       pick = restaurants[rand]
                       print(pick)
                       end()
run()
fv.close()
