from typing import Union
from collections.abc import Sequence

from Restaurant import Restaurant

class RestaurantList(Sequence):
    restaurant_list: list[Restaurant]

    def __init__ (self, food_list: Union[list[Restaurant], Restaurant] = list()):
        if isinstance(food_list, Restaurant):
            self.restaurant_list = list((food_list))  # do we need a single or double ()
        else:
            self.restaurant_list = food_list

    def __getitem__(self, idx):
        return self.restaurant_list[idx]
    
    def __len__(self):
        return len(self.restaurant_list)

    @property
    def restaurant_list(self) -> list[Restaurant]:
        return self.restaurant_list
    
    def clone(self) -> list[Restaurant]:
        copyList: list[Restaurant] = RestaurantList()
        for i in self.restaurant_list:
            copyList.append(i.clone())
        return copyList
    
    def append(self, new_restaurant: Restaurant) -> None:
        self.restaurant_list.append(new_restaurant)


    

