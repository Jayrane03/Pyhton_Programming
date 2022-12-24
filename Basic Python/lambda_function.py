# The power of lambda is better shown when you use them as an anonymous function inside another function.

#  Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a : a+ 20
print(x(4))



def myFunc(n):
    return lambda a : a*n


mydouble  = myFunc(20)
print(mydouble(3))