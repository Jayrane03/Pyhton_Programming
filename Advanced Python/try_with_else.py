from re import I


try:
    i = int(input("Enter a number :"))
    c = 1/I
except Exception as e:
    print(e)
else:
    print("We were successful")
    
# Some times we want to run program when try was successful then the else is used with try block


