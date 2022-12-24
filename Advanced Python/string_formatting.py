# from calendar import formatstring


# # Sting formaatting
# price = 300
# amount = 302
# txt = "This {}price is in {:.2f} dollars" #it is used to show the price in decimal format
# print(txt.format(price ,amount))


from xml.dom import IndexSizeErr


age = 19
name = "Jay"
#  this is used to print the variables by their index numbers like age is first so its number is 0 and name index is 1

txt = "My name is {1}. {1} is {0} years old"
print(txt.format(age,name))


# named Index
myorder = "I have a {carname} , it is a {model} "
print(myorder.format(carname = "ford" , model = "Mustang"))


foodItem ="This is {typeofdrink} of {teaname}"
print(foodItem.format(typeofdrink = "tea" , teaname = "Agaani"))