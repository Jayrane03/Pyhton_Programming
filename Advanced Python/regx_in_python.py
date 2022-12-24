# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.


# RegEx can be used to check if a string contains the specified search pattern.
import re
from traceback import print_tb
txt = "This is a train that is going to Dadar"
x = re.search("Dadar" ,txt)
if x:
    print("Yes we have a match!")
    
else:
    
    
    print("No match found!")
# The search() function searches the string for a match, and returns a Match object if there is a match.

# If there is more than one match, only the first occurrence of the match will be returned:
    
txt2 = "The rain in Spain ."
x2 = re.search("S", txt2)
# s = whitespace 
print("The first white-space character is located in position:", x2.start())



# This are some functions in regex

# sub 
txte = " this is a rainy season"

r = re.sub("\s", "30" , txte)
print(r)

# find alll function

d = re.findall("i" , txte) # it will show how many i are present in the string and print it in a list 
print(d)
c = re.split("\s" ,txt,2) # -- this will Split the string only at the second occurrence:
print(c)

# check if the string has arn in it and print it in a list format 
# e = re.findall("[arn]",txte)
e = re.findall("[a-s]" , txte) # print the aplhabets between a and s in a list
print(e)


