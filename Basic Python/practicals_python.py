
# li = [1,2,3,43]
# # x = li.append(2)
# print(li)

# y = li.extend()
# print(li)

# class Student:
#     name:'Jay';
#     roll_number:33;
    
#     def setAge(init):
#          age = input("Enter your name ")
#          print("Student Age is :-",age)
        
#     def setMarks(init):
#         marks=input("Enter your marks in percentage")
   
        
#     def displayDetails(init)


        


# stu = Student()
# stu.setAge()  
# stu.setMarks()
# stu.displayDetails()

class Numbers:
    def one_t_fifty_numbers(self):
        for i in range(1,51):
            print("Numbers from 1-50 :",i)
            
            
    def even(self):
        for num in range(1,51):
            if(num%2==0):
              print(num)
              
    def odd(self):
         for num in range(1,51):
            if(num%2!=0):
              print(num)
              
no =Numbers()
print("Numbers from 1-50 are :")
no.one_t_fifty_numbers()
print("Even numbers are")
no.even()
print("Odd numbers are")
no.odd()
# no.odd()