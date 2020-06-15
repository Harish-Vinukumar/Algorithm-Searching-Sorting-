"""
 Linear search or sequential search is a method for
 finding an element within a list. It sequentially
 checks each element of the list until a match is
 found or the whole list has been searched.
"""


def linear_search(array, key):
    for x in array:
        if x == key:
            return array.index(x)


array = [1, 7, 8 , 10, 15, 19, 23, 26, 27]

print(linear_search(array, 15))