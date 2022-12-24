def missingElement(my_arr,n):
    exp_sum = num_of_ele *(num_of_ele+1) /2
    actual_sum =sum(my_arr)
    
    return exp_sum - actual_sum    




if __name__ == "__main__":
    
    my_arr = []
    
    num_of_ele = int(input("Enter the total number of element \n"))
    
    for i in range(num_of_ele-1):
        array = int(input("Enter the element in the array \n"))
        my_arr.append(array)
        

missing_number  = missingElement(my_arr,num_of_ele)
print("The missing element in the above array is{}".format(missing_number))
        