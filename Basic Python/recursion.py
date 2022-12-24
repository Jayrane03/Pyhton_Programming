import numbers


# factorial of a numbers
# recursion is a function which called itself. It is used to directly used mathematical formula as a function

def fact_recursive(n):
    if n==1 or n==0:
        return 1;    
    return n*fact_recursive(n-1)
    
f= fact_recursive(5)
print(f) 
