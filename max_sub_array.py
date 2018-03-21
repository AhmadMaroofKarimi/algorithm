import math as m
import pdb

def cros_max_subarray(given_array, l_index, mid_index, r_index):
    """
    This function calculates the max sub array on both side of the mid points
    """
    #Assign very large negative number, -infinity
    l_sum = m.exp(50)*(-1)  
    i = mid_index; temp_sum = 0
    while (i >= l_index):
        temp_sum = temp_sum + given_array[i]
        if temp_sum > l_sum:
            l_sum = temp_sum
            left_cros_index = i
        i -= 1
    r_sum = m.exp(50)*(-1)
    temp_sum = 0; j = mid_index + 1
    while (j <= r_index):
        temp_sum = temp_sum + given_array[j]
        if temp_sum > r_sum:
            r_sum = temp_sum
            right_cros_index = j
        j += 1
    return left_cros_index, right_cros_index, r_sum + l_sum

def max_subarray(given_array,l_index,r_index):
    """
    This is the main function that calculates maximum sub-array problem.
    The function uses divide and conquer algorithm to solve this problem.
    The three probabilities of the maximum sub array is: on the left of the midpoint,
      on the right of the mid point, and across the mid-point partly on both sides.
    Initial value passed to the function are:
      (i)   array
      (ii)  0
      (iii) length of array -1 or the last index of the array  
    """
    if l_index == r_index:
        return l_index, r_index, given_array[l_index]

    mid_index = int(m.floor((l_index + r_index )* 0.5))
    
    left_low_ind, left_high_ind, left_sum = \
        max_subarray(given_array, l_index, mid_index)
    right_low_ind, right_high_ind, right_sum = \
        max_subarray(given_array, mid_index+1, r_index)
    cros_left_ind, cros_right_ind, cros_sum = \
        cros_max_subarray(given_array,l_index,mid_index,r_index)
    
    if left_sum >= right_sum and left_sum >= cros_sum:
        return left_low_ind, left_high_ind, left_sum
    elif cros_sum >= right_sum and cros_sum >= left_sum:
        return cros_left_ind, cros_right_ind, cros_sum
    else:
        return right_low_ind, right_high_ind, right_sum

pdb.set_trace()
g_array = [-4, 8, 6, -4, 1, 2]
l_ind = 0
r_ind = 5
print(max_subarray(g_array, l_ind, r_ind))
