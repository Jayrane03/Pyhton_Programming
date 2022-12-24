



# # while loop 
# i = 0;
# while i<10:
#     print("Yes" + str(i))
#     i = i+1
    
#     print("Done !")


fruits = ["Banana" , "Apple" , "Mango", "PineApple"]
# 
 
# for loop  in python are  use to iterate through a seqence such as list , tupple or string
# Range include (start,stop,step size)   for example 2 = step size then after one it will leave 2 gap
# for i in (fruits):
    
#     print(i)
    
    
    
    # for loop with optional else  - - it execute only successfully execution of for loop
    
for i  in range(10):
 print(i)
else:
    print("The for loop is over now")
    
    
    # for with break it is used to break the loop now
    #  else part will not get execute if the whole for loop is not get executed
for i in range(10):
    print(i)
    if i ==8:
        break 
    
    
    
    
    # continue with for
    
for i in range(20):
 
 if i == 5:
    print("Hello  guys")
    continue  
    print(i)
  