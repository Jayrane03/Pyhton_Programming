# sets ignore reptition  they look similar to dictionary

from traceback import print_tb


a = {1,2,3,4,5,2}  # here 2 will not get print again 
print(type(a))
print(a)

# b= {} -- this is an empty dictionary
b = set()  # this is an empty set 

# we can add and remove elements in our empty set by set methods

b.add(2); # adds the element
b.add(4);
b.add(3);
# we cannnot add list in set because it can be changed but we can add tupple
b.add((5,6,7,8))
b.remove(2) # removes the particular element in the set 
# b.clear() # it clears all elements in the set 
b.update()
b.intersection()
print(b)


s = {}
print(len(s)) 


