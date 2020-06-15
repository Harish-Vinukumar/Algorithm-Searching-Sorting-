"""
Binary search, also known as half-interval search,
logarithmic search, or binary chop, is a search
algorithm that finds the position of a target
value within a sorted array. Binary search
compares the target value to the middle element
of the array.
"""


def binary_search(array, l, r, key):
    middle = (l + r-1)//2
    if array[middle] == key:
        return middle
    elif array[middle] < key:
        return binary_search(array, middle + 1, r, key)
    else:
        return binary_search(array, l, middle - 1, key)


array = [1, 7, 8 , 10, 15, 19, 23, 26, 27]
num = len(array)
print(binary_search(array, 0, num, 26))