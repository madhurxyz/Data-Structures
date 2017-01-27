#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests below
    #If item is in index = 0, we have found the base case
    try:
        if array[index] == item:
            return index

    #Try/Except was the only way I found to handle IndexError
    except IndexError:
        return None

    #recursive function
    return linear_search_recursive(array, item, index + 1)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests below
    left = 0
    right = len(array) - 1
    found = False
    half = 0

    while left<=right and not found:
        half = (left+right)/2
        if array[half] == item:
            found = True
        elif item < array[half]:
            right = half - 1
        elif item > array[half]:
            left = half + 1

    if found:
        return half
    elif not found:
        return None

def binary_search_recursive(array, item, left=None, right=None):
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests below
    if left is None and right is None:
        left = 0
        right = len(array) - 1

    if left is not None and right is not None:
        half = (left+right)/2

    if array[half] == item:
        return half
    elif item < array[half]:
        return binary_search_recursive(array, item, left, half - 1)
    elif item > array[half]:
        return binary_search_recursive(array, item, half + 1, right)

    return None
