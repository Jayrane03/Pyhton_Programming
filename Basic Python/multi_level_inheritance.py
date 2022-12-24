#  When a child class become a parent of another child class then it is called as multilevel inheritance


class Person:
    country = "India"
    
    def takeBreak(self):
        print("I am  breathing...")
    
class Employee(Person):
    company = "Honda"
    
    def getSalary(self):
        print(f"Salary is {self.salary}")
        
    def takeBreak(self):
        print("I am an employee so I am luckily breathing..")        


class Programmer(Employee):
    company = "Fiver"
    
    
    def getSalary(self):
        print(f"No salary to the programmer")
        
        
p = Person()
p.takeBreak()
e = Employee()
pr = Programmer()