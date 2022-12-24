from itertools import count
from telnetlib import PRAGMA_HEARTBEAT


class Employee:
    country = "India"

    def showDetails(self):
        name = "Jay"
        print(f"The name of the employee is {self.name}")
        
class Person():
    country  = "America"
    city = Mumbai
    def showDetails(self): 
            name = "Omkar"
    print("I am a  boy")
    
class Programmer(Employee, Person):
      pass
  
  
e = Employee()   
p = Programmer()
print(p.country)