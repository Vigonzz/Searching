# Violet Gonzalez. SWE 241P 
#Assignment 2:
# Part 1:
# Given an array of integer nums sorted in non-decreasing order, 
# find a given target value's first and last position. Suppose the target
# is not found in the array; return [-1, -1]. You must write an algorithm with 
# O(log n) runtime complexity.  Also, write additional sample test cases to 
# validate your implementation.


def _binary_search_bound(arr, target, find_first):
    low = 0
    n = len(arr)
    high = n - 1
    result = -1

    # narrow the search range until it is empty
    while low <= high:
        mid = (low + high) // 2 
        # Case 1:
        if arr[mid] < target: 
            low = mid + 1
        # Case 2:
        elif arr[mid] > target:
            high = mid - 1
        # Case 3:
        else:
            result = mid
            if find_first:
                high = mid - 1
            else:
                low = mid + 1
        return result

def find_start_end(arr, target):
    start = _binary_search_bound(arr, target, find_first=True)
    end = _binary_search_bound(arr, target, find_first=False)

    return [start, end]

