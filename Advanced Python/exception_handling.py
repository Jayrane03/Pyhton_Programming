
# # try :
# #     print(x)
    
# # except NameError:
# #     print("Variable x is not defined")
    
# # except:
# #     print("An exception has occured")
    
# # else:
# #     print("Nothing went wrong")

# #  from re import L

# #  try to wite and open a file which is unopenable and not writable
# try :
#    f = open("demon.txt")
#    try:
#     f.write("Lorem Ispsum")
    
#    except:
#        print("Something went wrong while writing into the file ")
#    finally:
#        f.close()
# except:
#      print("Something went wrong while opening the file ")
       

# x = -1
# if x<0:
#     raise Exception("Sorry , no numbers below zero")
# # The raise keyword is used to raise an exception.
# # You can define what kind of error to raise, and the text to print to the user.

# y = "Hello"

# if not type(y) is int:
#     raise TypeError("Only integers are allowed  ")


# while(True):
#     print("Press q to quit")
#     a =input("Enter a number \n")
#     if(a=='q'):
#         break
#     try:
#         a=int(a)
#         if a>6:
#             print("You enter a number grater than 6")
#     except Exception as e:
#         print(e)
# print("Thanks for playing this game")

# from ast import keyword


# try:
#     a=int(input("Enter a number \n"))
#     c= 1/a
#     print(c)

# except ValueError as e:
#     print("Please enter a correct value")
    

# except ZeroDivisionError as ee:
#     print("Make sure that you are not dividing the number by zero")
    
# print("Thanks for using this code")


# Raising exeception using raise keyword 



# def incremeent(Num):
#     try:
#         return int(num)+1
#     except:
#         raise ValueError("This is not good - Jay")
    
# a= incremeent('232') # here 232 is a string so it will through the value error which is raised by us
# print(a)


# try with else _Statement

