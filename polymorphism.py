class Shape:
    
    def area(self,redius,l,b):
        if b==None:
         print("radious")
         return 3.14*redius**2
        else:
            print("multiply")
            return l*b
    
    # def area(self,l,b):
    #     return l*b
    
    # in python polymorphism is not avilable
s=Shape()
s.area(redius=2,b=None,l=None)
s.area(redius=34,b=4,l=5)
# s.area(3)