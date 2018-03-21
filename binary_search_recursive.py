import math as m

def binary_search(sorted_array, value, pre_index, post_index):
    """
    
    """
    if ( pre_index >= post_index):
        #terminating condition

        if pre_index > post_index:
            return False
        elif(sorted_array[pre_index] == value ):
            return pre_index
        else:
            return False
    
    mid_index = int(m.floor((pre_index + post_index)/2))
    if (value > sorted_array[mid_index]):
        ind = binary_search(sorted_array,value, mid_index+1, post_index)
    elif(value < sorted_array[mid_index] ):
        ind = binary_search(sorted_array, value, pre_index, mid_index)
    elif (value == sorted_array[mid_index]):
        return mid_index

    return ind 
    
sorted_array = [2,3,4,6,7]
value = 7
pre_index = 0
post_index = 4
index = binary_search(sorted_array, value, pre_index, post_index)    
print(index)
