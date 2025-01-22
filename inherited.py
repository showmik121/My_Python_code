class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone construstor")
        self.__price=price
        self.brand=brand
        self.camera=camera
        
    def buy(self):
        print("Buying a Phone!")
        
    def get_price(self):
        return self.__price
        
class Smartphone(Phone):
    def __init__(self, os, ram,price,brand,camera):
        super().__init__(price, brand, camera)
        super().buy()
        self.os=os
        self.ram=ram
        print("Inside smartphone construstor")
        
        
    def print_pr(self):
        print(self.get_price())

s=Smartphone("apple",3, 200000, "apple", 3)
s.buy()
print(s.brand)
s.print_pr()
