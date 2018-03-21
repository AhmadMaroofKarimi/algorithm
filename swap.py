def swap(given_array,i,j):
    """
    given_array: Array in which swapping is to be done.
    i: one of the index to be swaped
    j: other index to be swaped with i
    """
    if len(given_array) >= i and len(given_array) >= j:
        temp = given_array[i]
        given_array[i] = given_array[j]
        given_array[j] = temp
        return given_array
    else:
        return False

