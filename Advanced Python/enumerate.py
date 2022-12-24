# from ast import comprehension


# list1= [ 3,4,5,443,False,9.3,"Jay"]
# index = 0
# for item in list1:
#     print(item , index)
#     index += 1
# The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.
# for index , item in enumerate(list1):
#     print(item , index)
    
    
# list comprehension

a = [2,342,43,32,32,1,67,89,102]
# b=[]
# for item in a:
#     if item%2==0:
#         b.append(item)

# print(b)
    
    
    # shortcut for this
    
b = [i for i in a if i%2==0]
print(b)