from typing import Union

class Restaurant:
    name: str
    price: float
    vegan: bool
    region: str
    type: list[str]

    def __init__(self, name, price, vegan, region, type):
        self._name = str(name)
        self._price = float(price)
        self._vegan = bool(vegan)
        self._region = str(region)
        self._type = type
        return

    def clone(self):
        return Restaurant(self._name, self._price, self._vegan, self._region, self._type)
    
    def __str__(self):
        '''
        Prints a list of restaurant attributes
        Use: print(source)
        Use: s = str(source)
        '''
        if self._vegan is True:
            veg_status = 'Vegan'
        else:
            veg_status = 'Not Vegan'
        s = (f'''Restaurant:
Name: {self._name}
Price: {self._price}
{veg_status}
Region: {self._region}
Type: {self._type}''')
        return(s)

    @property
    def name(self):
        return self._name
    
    @property
    def price(self) -> float:
        return self._price
    
    @property
    def vegan(self) -> bool:
        return self._vegan
    
    @property
    def region(self) -> str:
        return self._region
    
    @property
    def type(self) -> list[str]:
        return self._type
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @price.setter
    def set_price(self, new_price:float) -> None:
        self._price = new_price

    @vegan.setter
    def set_vegan(self, is_vegan: bool) -> None:
        self._vegan = is_vegan

    @region.setter  
    def set_region(self, new_region: str) -> None:
        self._region = new_region

    @type.setter
    def set_type(self, new_types: list[str]) -> None: 
        self._type = new_types

    def appendType(self, new_type: str) -> None:
        self._type.append(new_type)

    

        

