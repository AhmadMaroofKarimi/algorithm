import swap as s
import sys
import pdb

def insertion_sort(given_array, index):
    """
    In this insertion sort algorith, I have tried to used 
    recurssion method, I could have easily used "for loop"
    but I wanted to practice recursion.

    The main fucntion starts with given array and index value of 0.
    recursively we increase the value of index and also the values 
    in the given array gets sorted for previous indeices.
    """
    if len(given_array) <= index:
        print( index)
        return given_array

    i = index
    while i > 0:
        #here I check for all of n-1 indices to make sure 
        # value at given at index is smallest in all the preceeding index.
        #So, I check until the value in the given index becomes smallest.  
        if given_array[i] < given_array[i-1]:
            s.swap(given_array,i-1,i)
            i -= 1
        else:
            # if any intermediate index has value not larger than the given index
            # then for sure all the preceding index will have values less than the given index.
            break
    #commented section intutively make more sense to me bu it same as the following return statement
    #arr = insertion_sort(given_array,index+1)
    #return arr
    return insertion_sort(given_array,index+1)

pdb.set_trace()

given_array = [3,2,1,6,1,1,9,2,13]
ind = 0
sorted_array = insertion_sort(given_array , ind)
print(sorted_array)
