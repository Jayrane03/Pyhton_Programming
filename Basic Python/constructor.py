#  from copyreg import constructor
# from platform import python_branch


# __iniself in Python class. self represents the instance of the class. By using the “self” keyword we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.t__ constructor in  python it will run automatically 
   


from ast import Delete, keyword
from mimetypes import init
from msilib import PID_REVNUMBER

 
class Student:
    def __init__(self,name):
       self.name = name
       
    def  getSalary(self):
          print("Hello world")        
        
        
init = Student("Jayu")  #--  Object can be instantiated by using constructor like this 


class Person:
    def __init__(self, name , age):
        self.name = name
        self.age =  age
        
        
    def myFunc(self):
      print("Hello my name is "+self.name)
      print("I am "+self.age)
      
p1 = Person("Jay" , str(56))
p1.myFunc()      
        
        
        
        # Delete keyword  -- you can delete object by usinf this keyword
        # del p1
        
