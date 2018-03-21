import math
import pdb

def max_sub_array(given_array, l_index, r_index):
    temp_sum = math.exp(50)*(-1)
    for i in range (0,r_index):
        sub_array_sum = 0
        for j in range (i, r_index):
            sub_array_sum += given_array[j]
            if temp_sum < sub_array_sum:
                temp_sum = sub_array_sum
                index_low = i
                index_high = j
    return temp_sum, index_low, index_high

#pdb.set_trace()
g_array = [-4, 8, 6, -4, 5, -2]
l_ind = 0
r_ind = 6
print(max_sub_array(g_array, l_ind, r_ind))
    
