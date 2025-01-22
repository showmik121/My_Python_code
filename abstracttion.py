from abc import ABC, abstractmethod

class Bankserver(ABC):
    def database(self):
        print("Connected to the database")
        
    @abstractmethod
    def security(self):
        pass  # Abstract methods cannot have an implementation
    
    @abstractmethod 
    def display(self):
        pass  # Abstract methods cannot have an implementation

class Mobileapp(Bankserver):
    def mobile_login(self):
        print("Mobile app login successful")
        
    def security(self):
        print("Mobile app security passed")
       
    def display(self):
        print("Displaying data from the mobile app")
       
# Instantiate the child class
mob = Mobileapp()
mob.mobile_login()
mob.database()
mob.security()
mob.display()
