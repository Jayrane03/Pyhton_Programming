# from multiprocessing import parent_process


class Employee:
    company = "Google"

    def showDeatils(self):
        print("This is ae employee")

class Programmer(Employee):
    language = "Python"
    def getLanguage(self):
        print(f"The language is {self.language}")
    
e = Employee()
e.showDeatils()
p = Programmer()
p.showDeatils()
print(p.company)
# print(e.language)

# Multiple Inheritance 
#  two parent and single child class


# Multi-level inheritance
    # parent
    # Child1
    # Child2