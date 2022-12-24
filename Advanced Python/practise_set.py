# l = [1,2,3,4,5,6,7,8,9,10] 
# for index , item in enumerate(l):
#     if index==2 or index==4 or index==6:
#         # print("Index is :",index,"| Number is :",item)
#         print(f"The {index}th element is {item}")
#


#  print a table using list comprehension
num = int(input("Enter the number  \n"))

table = [num*i for i in  range(1,11)]
print(table)

with open("tables.txt","a") as f:
    f.write(str(table))
    f.write('\n')

# num1 = int(input("Enter a number one \n"))
# num2 = int(input("Enter the number two \n"))

# li = [num1 , num2]
# print(li[0],li[1])
