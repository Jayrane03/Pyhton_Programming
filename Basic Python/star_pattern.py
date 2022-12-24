# This pattern program
# *
# **
# ***
# ****

# n = int(input("Enter the number of rows "))

# for i in range(n):
#     print("*" *(i+1))
'''

   *
  ***
 *****
 This program 
 for loop will print the number of rows 
 1 print will print the before spaces and the end is use to not print a new line
 as the number of rows will increasing number of spaces will decrease
 2 print  will  print the stars according to the requirement in the rows such in 1-one star ,2- three star so formula is 2 multiply by i (each row) + one that will give us the odd number as the stars 
 3 print will print the after spaces 
'''


rows  = int(input("Enter the number of rows "))
for i in range(rows):
    print(" " *(rows-i-1),end="")
    print("*" *(2*i+1),end="")
    print(" " *(rows-i-1))

