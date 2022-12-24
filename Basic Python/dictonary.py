# '''
#   Dictionary are unordered
#   they are mutable can be changed
#   it is indexed 
#   cannot contain duplicate key
# '''


from argparse import ONE_OR_MORE


myDict = {
    
  "Fast" : "In a quick mannner",
  "Jay"  : "A coder",
  "Marks": [1,32,3,4,234],
  "anotherDict" : {'Harry' : 'Player'},
  3 : 4
}

# print(myDict['Fast'])
# print(myDict['Marks'])
# print(myDict['anotherDict'] ['Harry'])

# # Dictionary Methods



# print(myDict.keys()) # will print the key in a form of  list
# print(myDict.values()) # will print the value in a form of  list
# print(myDict.items()) # it will  print the (key , value) in the form of  list but it will not be a list
 
 
newDict = {
   "Romania" : " Jungle" ,
   "Divya"   : "Friend" ,
       "Jay"  : "A fighter" 
 }

# myDict.update(newDict) #updates the old dictionary by adding key values from new dictionary
# print(myDict)
# Get method
print(myDict.get("jay")) # this will return none if the key value is not in the dictionary
print(myDict['Jay']) # this will throw an error as the key value is not in the dictionary 



# practice set question ONE
translation = {
  "Good Boy" : "Accha Ladka",
  "Bad Boy"  : "Bura Ladka",
  "Cat"      : "Billi",
  "Dog"      : "Kutta",
  "Love"     : "Pyaar"
    
}
print("Choose any one from this :" , translation.keys())

a = input("Enter the word you want to translate :\n")
print("The meaning of the word you entered is : " , translation.get(a))
