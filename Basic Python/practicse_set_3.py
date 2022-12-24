# ques 1 write a program to accept fruits in a list and  print the list
# f1 = input("Enter the fruit number 1 \n")
# f2 = input("Enter the fruit number 2 \n")
# f3 = input("Enter the fruit number 3 \n")
# f4 = input("Enter the fruit number 4 \n")
# f5 = input("Enter the fruit number 5 \n")
# f6 = input("Enter the fruit number 6 \n")
# f7 = input("Enter the fruit number 7 \n")
# my_fruit_list = [f1 ,f2 ,f3,f4,f5,f6,f7]

# print("The fruit list are : " + my_fruit_list)

# quest 2 take 6 students marks in a list and sort them in order
st1 = int (input("Enter the marks of student Roll no 1 : "))
st2 = int (input("Enter the marks of student Roll no 2 : "))
st3 = int (input("Enter the marks of student Roll no 3 : "))
st4 = int (input("Enter the marks of student Roll no 4 : "))
st5 = int (input("Enter the marks of student Roll no 5 : "))
st6 = int (input("Enter the marks of student Roll no 6 : "))

marks = [st1 , st2 , st3, st4 , st5 , st6 ]
marks.sort()
print(sum(marks))
print(marks)
