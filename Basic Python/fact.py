from math import factorial
import numbers


# factorial of a numbers
#  This is  a program of printing all the factorials till the number enter by the user 

# num = int(input("Enter a number to find it's factorial \n"))
# fact = 1;
# for i in range(1,num+1):
#     fact = fact * i
#     print(f"The factorial of {i} is {fact}" )
    
    
    #  this is the program of printing only one factorial of the number entered by the user 
num = int(input("Enter a number to find it's factorial \n"))
fact = 1;
for i in range(1,num+1):
    fact = fact * i
print(f"The factorial of {i} is {fact}" )



