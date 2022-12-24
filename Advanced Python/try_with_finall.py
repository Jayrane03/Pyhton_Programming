
# Python offers a finally clause which ensures execution of a piece of code irrespective of the exception\
# finally will executed also regard the program is exit

try:
    i = int(input("Enter a number :"))
    c = 1/i
except Exception as e:
    print(e)
    exit()
finally:
    print("We were done")
    
    
        
    