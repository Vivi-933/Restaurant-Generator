from typing import Self, Union

class Restaurant:
    name: str
    price: float
    vegan: bool
    region: str
    type: list[str]

    def __init__(self, name: str, price: float, vegan: bool, region: str, type: list[str]):
        self.name = name
        self.price = price
        self.vegan = vegan
        self.region = region    
        self.type = type

    def clone(self) -> Self:
        return Restaurant(self.name, self.price, self.vegan, self.region)
    
    def __str__(self):
        '''
        Prints a list of restaurant attributes
        Use: print(source)
        Use: s = str(source)
        '''
        if self.vegan:
            veg_status = 'Vegan'
        else:
            veg_status = 'Not Vegan'
        print('''Restaurant:
        Name: {self.name}
        Price: {self.price}
        {veg_status}
        Region: {self.region}
        Type: {self.type}
              ''')
        return

    @property
    def name(self) -> str:
        return self.name
    
    @property
    def price(self) -> float:
        return self.price
    
    @property
    def vegan(self) -> bool:
        return self.vegan
    
    @property
    def region(self) -> str:
        return self.region
    
    @property
    def type(self) -> list[str]:
        return self.type
    
    @name.setter
    def set_name(self, new_name:str) -> None:
        self.name = new_name

    @price.setter
    def set_price(self, new_price:float) -> None:
        self.price = new_price

    @vegan.setter
    def set_vegan(self, is_vegan: bool) -> None:
        self.vegan = is_vegan

    @region.setter  
    def set_region(self, new_region: str) -> None:
        self.region = new_region

    @type.setter
    def set_type(self, new_types: list[str]) -> None: 
        self.type = new_types

    def appendType(self, new_type: str) -> None:
        self.type.append(new_type)

    

        

