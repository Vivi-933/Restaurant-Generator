"""Contains the RestaurantList class"""
from typing import Union
from collections.abc import MutableSequence

from Restaurant import Restaurant

class RestaurantList(MutableSequence):
    """Holds Restaurant objects for manipulation"""
    restaurant_list: list[Restaurant]

    def __init__ (self, food_list: Union[list[Restaurant], Restaurant] = None):
        """Initializes a new instance of the class RestaurantList"""
        if food_list is None:
            food_list = []

        if isinstance(food_list, Restaurant):
            self.restaurant_list = list((food_list))  # do we need a single or double ()
        elif (isinstance(food_list, list[Restaurant])) :
            self.restaurant_list = food_list

    def __getitem__(self, idx: int):
        return self.restaurant_list[idx]
    
    def __len__(self):
        return len(self.restaurant_list)
    
    def __delitem__(self, idx: int):
        self.restaurant_list.pop(idx)

    def __setitem__(self, idx: Union[int, slice], value: Union[Restaurant, slice]):
        self.restaurant_list[idx] = value

    @property
    def restaurant_list(self) -> list[Restaurant]:
        """get the restaurant_list"""
        return self.restaurant_list.clone()
    
    def clone(self) -> list[Restaurant]:
        """Makes a copy of the restaurant_list"""
        copy_list: list[Restaurant] = RestaurantList()
        for i in self.restaurant_list:
            copy_list.append(i.clone())
        return copy_list
    
    def insert(self, index: int, value: Restaurant):
        """inserts new object at index"""
        self.restaurant_list.insert(index, value)

    

