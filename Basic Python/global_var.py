
a= 54 # it is a Global variable 

def func1():
    global a
    print(f"Print Statement 1 : {a}")
    a =4  #-- this is a ;local variable
    print(f"Print Statement 2 : {a}")
    
func1()
print(f"Print Statement 3 : {a}")