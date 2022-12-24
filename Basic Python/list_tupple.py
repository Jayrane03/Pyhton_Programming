# This  is a list create a list  using []
from operator import index


a = [1,2,34,43,54]
print(a[2])
# You can change any value in the list
a[2] = 102
print(a[2])
print(a)
# A list can be of multiple data types mixture of it

c= [223 , "Jay" , False , 82.22]
print(c)


# List Slicing

# friends = ["Jay" , "Omkar" , "Rohan" , "Joy" , "Jane" , 33]
# print(friends[0:4]) # it will print the value from index number 0-4 
# print(friends[-4: -3]) #it will count from back onwards  and print from rohan



# a.sort(); # to print the list in ascending order
# print(a)
# a.reverse()
# print(a) #print  from big to small
# a.append(3)
# print(a) #it will add an element in the list 
# a.insert(3,4)  #this will add 4 at 3rd index
# print(a)    
# a.pop(2) #This will delete the element at the index no 2 and print the rest of the list as it is
# print(a)
# a.remove(102) #It is used to remove the particular elementthr md
# print(a)




# Tuple -- it cannot be updated - it is immutable data type in python

t = (1,2,3,4,1,1,2,1,21)
print(t[0])
for x in (t):
    print(x)

# t[0] = 23  cannot be changed
t1 = () # empty tuple
t1 = (1,) # tuple with single element
print(t1)

# Tuple methods
# print(t.count(1))   return the number of occurance of value
# print(t.index(3)) it will print the index number of the element
