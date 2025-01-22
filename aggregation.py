class Customer:
    def __init__(self,name,gander,adress):
        self.name=name
        self.gander=gander
        self.adress=adress
        
        
    def print_info(self):
        print(f"Name: {self.name}, Gander: {self.gander}, Adress: {self.adress.get_city()}, {self.adress.pin}, {self.adress.state}")
        
class Adress:
    def __init__(self,city,pin,state):
        self.__city=city
        self.pin=pin
        self.state=state
        
        
    def get_city(self):
        return self.__city
        
add=Adress("gazipur","1213","Dhaka")
cus=Customer("showmik","Male",add)
cus.print_info() 