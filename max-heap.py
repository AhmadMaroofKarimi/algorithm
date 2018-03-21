import swap as s
import math as m

def max_heapify(arr, index, arr_len):
    l_chld = 2*index + 1
    r_chld = 2*index + 2
    
    if l_chld < arr_len and arr[l_chld] > arr[index]:
        largest_val_index = l_chld
    else:
        largest_val_index = index

    if r_chld < arr_len and arr[r_chld] > arr[largest_val_index]:
        largest_val_index = r_chld
    if largest_val_index != index:
        arr = s.swap(arr,largest_val_index,index)
        max_heapify(arr,largest_val_index,arr_len)
    return arr

def max_heap_sort(arr):
    a_len = len(arr)
    i = int(m.floor(a_len/2)) - 1
    while (i >= 0):
        sorted_arr = max_heapify(arr, i, a_len)
        i -= 1
    return sorted_arr

import pdb
pdb.set_trace()

given_array = [3,2,1,6,1,1,9,2,13]
print(max_heap_sort(given_array))
        
