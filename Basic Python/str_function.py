from traceback import print_tb


story = "this is a short story with title You and me are same ? "
# String Function 
print(len(story))  #to find the length of the string
print(story.endswith(" ")) # to find the last letter of the string
print(story.startswith("This")) #to find the first letter of the string
print(story.count("a"))  # to find how many alphabets are used in the string for eg how many 'a' are used
print(story.capitalize()) # to capitalize the first letter of the string
print(story.find("this")) # if  you get -1 then the word is not there in the string

print(story.replace("this","That")) # tot replace one word with another it replace all the occurance form the string

