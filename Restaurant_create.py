from Restaurant import Restaurant
def create_restaurant():
    print('Restaurant Attributes (input 0 to ignore prompt)')
    Name = input('Name of restaurant:  ')
    if Name == 0:
        Name = None
    Price = float(input('avg price: '))
    Price = float(round(Price, 2))
    if Price == 0:
        Price = None
    veg = input('Vegan options?(T/F) ')
    if veg == 'T':
        Vegan = True
    else:
        Vegan = False
    Region = input('Origin: ')
    if Region == 0:
        Region = None
    
    type = input('Food types(seperate by comma): ')
    type.split(',')
    fv = open('restaurants.txt', 'a', encoding = 'utf-8')
    fv.write(f'{Name}|{Price}|{Vegan}|{Region}|{type}\n')
    fv.close()
    return
