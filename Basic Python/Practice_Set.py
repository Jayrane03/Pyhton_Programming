# # Create a class Programmer and store his info in it 
# Question no -1 
# class Programmer:
    
#     def __init__(self,name,product) -> None:
#         self.name = name
#         self.product = product
        
        
#     def pinfo(self):
#         print(f"The name of the programmer is {self.name} and the product is {self.product}")
        
# jay = Programmer("Jay", "Face1book") 
# kswap = Programmer("K" ,"Skype")  
# jay.pinfo()  
# kswap.pinfo()  

# from ast import Num
# from cmath import sqrt


class Calculator:
    
    def __init__(self,num):
        self.number = num
        
    def square(self):
        print(f"The square of the number is {self.number **2}")
        
    def cube(self):
        print(f"The cube of the number is {self.number **3} ")
            
    def  squareRoot(self):
        print(f"The square root of the number is {self.number **0.5} ")
        
num = int(input("Enter a number "))
a = Calculator(num)
a.square()                      
a.cube()                      
a.squareRoot()                      


def showEmp():
    