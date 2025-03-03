# Imports
from Restaurant_create import create_restaurant
from Restaurant import Restaurant
from random import randint

# Files
fv = open('restaurants.txt', 'r', encoding = 'utf-8')

# Constants
OPTIONS = ['create restaurant', 'view restaurant',
            'find restaurant(all)', 'find restaurant(random)']
CRITERIA = ['price', 'vegan', 'region', 'type']


def end(res_list):
    '''
    Gives user option to end or continue program
    '''
    cont = input('Would you like to do anything else? (Y/N) ')
    if cont == 'Y':
        run(res_list)
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
    end(res_list)


def run(res_list):
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
        option1(res_list)
    # Brings up all restaurants matching user filter
    elif result == 2:
        print('What criterion would you like to filter by? ')
        option2(res_list)
    # brings up a random restaurant matching user filter
    elif result == 3:
        option3(res_list)

def option1(res_list):
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
                end(res_list)
        else:
            end(res_list)

def option2(res_list):
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
    matches = []
    if criterion == 1:
        filt = float(filt)
        matches = match_price(filt, res_list)
    elif criterion == 2:
        filt = bool(filt)
        matches = match_vegan(filt, res_list)
    elif criterion == 3:
        matches = match_region(filt, res_list)
    elif criterion == 4:
        matches = match_type(filt, res_list)
    else:
        print('Not an option')
        end(res_list)
    if matches != []:
        for i in matches:
            print(i)
        end(res_list)
    else:
        add = input('''no such restaurant exists.
Would you like to add it?(Y/N) ''')
        if add == 'Y':
            create_menu()
        else:
            end(res_list)


def option3(res_list):
    '''
    Brings up random restaurant matching user filter
    '''
    print('What criterion would you like to filter by? ')
    for i, crit in enumerate(CRITERIA):
        print(f'{i+1}: {crit}')
    criterion = int(input('Option: '))
    filt = input('Filter by: ')
    print()
    matches = []
    if criterion == 1:
        filt = float(filt)
        matches = match_price(filt, res_list)
    elif criterion == 2:
        filt = bool(filt)
        matches = match_vegan(filt, res_list)
    elif criterion == 3:
        matches = match_region(filt, res_list)
    elif criterion == 4:
        matches = match_type(filt, res_list)
    else:
        print('Not an option')
        end(res_list)
    if matches != []:
        ran = randint(0,len(matches)-1)
        res = matches[ran]
        print(res)
        end(res_list)
    else:
        add = input('''no such restaurant exists.
Would you like to add it?(Y/N) ''')
        if add == 'Y':
            create_menu()
        else:
            end(res_list)

def match_price(price,res_list):
    '''
    use: matches = match_price(price, res_list)
    '''
    matches = []
    for i in res_list:
        if i.price <= price:
            matches.append(i)
    return matches

def match_vegan(vegan,res_list):
    '''
    use: matches = match_vegan(veg,res_list)
    '''
    matches = []
    for i in res_list:
        if i.vegan == vegan:
            matches.append(i)
    return matches

def match_region(region,res_list):
    '''
    use: matches = match_region(price,res_list
    '''
    matches = []
    for i in res_list:
        if i.region == region:
            matches.append(i)
    return matches

def match_type(typ,res_list):
    '''
    use: matches = match_type(price,res_list)
    '''
    matches = []
    for i in res_list:
        if typ in i.type:
            matches.append(i)
    return matches

res_list = generate()
run(res_list)
fv.close()
