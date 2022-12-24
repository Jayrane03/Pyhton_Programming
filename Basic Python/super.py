    
    
#  When a child class become a parent of another child class then it is called as multilevel inheritance


class Person:
   
    country = "India"
    def  __init__(self):
        print("Initializing the Person") 
    def takeBreak(self):
        print("I am  breathing...")
    
class Employee(Person):
    company = "Honda"
    def  __init__(self):
        super().__init__()
        print("Initializing the Employee")
    def getSalary(self):
        print(f"Salary is {self.salary}")
        
    def takeBreak(self):
        print("I am an employee so I am luckily breathing..")        


class Programmer(Employee):
    company = "Fiver"
    def  __init__(self):
            super().__init__()
    print("Initializing the Programmer")
    
    def getSalary(self):
        print(f"No salary to the programmer")
        
    def takeBreak(self):
        super().takeBreak()
        print("I am an Programmer so I am luckily breathing..")       
        
        
# p = Person()  
# p.takeBreak()
# e = Employee()
# e.takeBreak()
pr = Programmer()
pr.takeBreak()