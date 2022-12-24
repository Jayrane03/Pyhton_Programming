import imp
from importlib.util import module_for_loader
import myModule
import platform  # it is a built in function

# x = platform.system()
# use can create a file and u can use that file as module
# myModule.greetMe("Jay")

# her age is taken from another module or file by importing that file
# a = myModule.person["age"]
# print(a)

# we can create allis by giving a short name to our file 
# such as
# import myModule as muy
# so we can use  ... muy.greetMe("jay")

x = dir(platform)
print(x)



y = dir(myModule)
print(y) 

# from keyword is used to import specific part of the module
# from myModule import greetMe then it will import only greetMe function