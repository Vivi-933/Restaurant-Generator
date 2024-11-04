from 
print('Restaurant Attributes (input 0 to ignore prompt)')
name = input('Name of food:  ')
if name == 0:
    name = None

price = float(input('avg price: '))
price = float(round(price, 2))
if price == 0:
    price = None

region = input('Origin: ')
if region == 0:
    region = None

