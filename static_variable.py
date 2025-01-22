class Atm:
    # static variable
    customer_id=1
    
    def __init__(self):
        self.pin=""
        self.__balance=0
        self.customer_id=Atm.customer_id
        Atm.customer_id+=1
        
        
c1=Atm()
print(Atm.customer_id)
c2=Atm()
print(Atm.customer_id)