"""
Bubble sort, sometimes referred to as sinking sort,
is a simple sorting algorithm that repeatedly steps
through the list, compares adjacent elements and
swaps them if they are in the wrong order.
The pass through the list is repeated until
the list is sorted.
"""


def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            if array[i] <= array[j]:
                array[i], array[j] = array[j], array[i]

    return array


array = [7, 8 , 5, 9, 10, 1, 55, 11, 8, 12]
print(bubble_sort(array))