
# # Use open function to read the content of a file 
# By default the mode is read mode
f = open('sample.txt','r')
data = f.read()
# data = f.read(5) -- it will read the first 5 letters  in the file 
print(data)
f.close()    


# # Write function 

# f = open('sample.txt' ,'w')
# f.write("Please add this line in the file ")
# f.close()


# use append method to not to override the text in the file
# f = open('sample.txt' , 'a')
# f.write("This is a part of appending")
# f.close()

# with in py  -- dont need to close the file with f.close()
# with  open('sample.txt', 'r') as f:
#      a = f.read()
#      print(a)
     

