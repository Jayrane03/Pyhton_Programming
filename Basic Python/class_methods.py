class Employee:
    #A Class method is a method which is bound to the class and not to the object of the class
    company = "JR Fitness Club"
    fees = 10000
    location = "Mumbai"
    
    # def changeFess(self, fee): 1st method to change class attribute
    #     self.__class__.fees = fee  # use __class__ is used to change the class attribute
    @classmethod  #decorator In Python, decorators are functions or classes that wrap around a function as a wrapper by taking a function as input and returning out a callable. They allow the creation of reusable building code blocks that can either change or extend behavior of other functions. 
    def changeFess(cls,fee):
        cls.fees =fee 
        
e = Employee()
e.changeFess(20000)
print(e.fees)
print(Employee.fees)


# An iterator is an object that contains a countable number of values.

# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

# myiter= "Banana"

# myit = iter(myiter)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))