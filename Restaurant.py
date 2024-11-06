"""Contains the Restaurant class that goes into the restaurant_list"""
from typing import Self, Union

class Restaurant:
    """Holds infromation about each restaurant"""
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
        """creates a copy of the current restaurant object"""
        return Restaurant(self.name, self.price, self.vegan, self.region, self.type)

    @property
    def name(self) -> str:
        """Name of the restaurant"""
        return self.name

    @property
    def price(self) -> float:
        """Average price of the restaurant"""
        return self.price

    @property
    def vegan(self) -> bool:
        """Tells if the restaurant is vegan"""
        return self.vegan

    @property
    def region(self) -> str:
        """The region the food is from"""
        return self.region

    @property
    def type(self) -> list[str]:
        """other attributes of the restaurant"""
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
        """Adds a new attribute to the restaurant"""
        self.type.append(new_type)
