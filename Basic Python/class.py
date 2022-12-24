# from traceback import print_tb


# class Employee:
#     company = "Google"
#     salary = 10000
    
    
# jay  =  Employee()
# omkar = Employee()
# omkar.company = "Microsoft"
# omkar.salary = 20000


# print(jay.company)  
# print(jay.salary)  

# print(omkar.company)  
# print(omkar.salary) 

class Employee:
    company = "Google"
    
    def get_salary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary} \n {signature}")
        
        
        @staticmethod
        def greet():
            print("Good Morning , Sir")
            
        @staticmethod
        def time():
            print("The time is 9am in morning")    

jay = Employee()
jay.salary =23000
jay.get_salary("Thanks !") # Employee.get_salary(jay)
jay.greet()  # Employee.greet() 
jay.time() 



