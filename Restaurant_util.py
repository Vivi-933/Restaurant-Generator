from Restaurant import Restaurant
from typing import Union

class RestaurantList:
    restaurant_list: list[Restaurant]

    def __init__ (self, food_list: Union[list[Restaurant], Restaurant] = list()):
        if isinstance(food_list, Restaurant):
            self.restaurant_list = list((food_list))  # do we need a single or double ()
        else:
            self.restaurant_list = food_list

    @property
    def restaurant_list(self) -> list[Restaurant]:
        return self.restaurant_list
    
    def clone(self) -> list[Restaurant]:
        copyList: list[Restaurant] = RestaurantList()
        for i in RestaurantList:
            copyList.append(i)
        return
    
    def append_list(self, new_restaurant: Restaurant) -> None:
        self.restaurant_list.append(new_restaurant)

    

