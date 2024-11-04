class Restaurant:
    Name: str
    Price: float
    Vegan: bool
    Region: str
    Type: []

    def __init__(self, name: str, price: float, vegan: bool, region: str):
        self.Name = name
        self.Price = price
        self.Vegan = vegan
        self.Region = region

    def getName(self):
        return self.Name
    
    def getPrice(self):
        return self.Price
    
    def getVegan(self):
        return self.Vegan
    
    def getRegion(self):
        return self.Region
    
    def setName(self, newName:str) -> None:
        self.Name = newName

    
        

