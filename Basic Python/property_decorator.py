class  Employee:
    company = "Bharat Gas"
    salary = 2000
    Bonus = 1000
    # totalSalray = 3000
    
    @property
    def totalSalary(self):
      return self.salary + self.Bonus
     
     
    @totalSalary.setter
    def totalSalary(self, val):
        self.Bonus = val - self.salary
        
        
 
e = Employee()
print(e.totalSalary) # this is a property so while calling the function we dont need to put ()
e.totalSalary = 5800
print(e.salary)
print(e.Bonus)

