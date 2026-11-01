# Violet Gonzalez. SWE 241P 
#Assignment 2:
# Part 1:
# Given an array of integer nums sorted in non-decreasing order, 
# find a given target value's first and last position. Suppose the target
# is not found in the array; return [-1, -1]. You must write an algorithm with 
# O(log n) runtime complexity.  Also, write additional sample test cases to 
# validate your implementation.


# AI transparency: Used claude code to better assist with understanding design choices, structure, and tests examples. 
# All code was produced by me!

def _binary_search_bound(arr, target, find_first):
    ''' Helper function that runs one binary search on a sorted array
      to locate one edge of the targets block, each search halves the range so it is O(log n). find_first picks the left or right edge
      and returns -1 if the target isn't found '''
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
    ''' Find the starting and ending positions of the target within the array '''
    start = _binary_search_bound(arr, target, find_first=True)
    end = _binary_search_bound(arr, target, find_first=False)

    return [start, end]


# Task 2:
def target_in_matrix(matrix, target):
    ''' The matrix can be identified as one sorted list therefore, 
    reading the matrix, row by row will give a sorted list and returns a true or false, it just converts mid 
    to row and column. The complexity is O(log(m * n)) '''

    if len(matrix) == 0:
        return False
    
    rows = len(matrix)
    cols = len(matrix[0])
    low = 0 
    high = (rows * cols) - 1

    # Narrow the search range for the matrix
    while low <= high:
        mid = (low + high) // 2
        row = mid // cols
        col = mid % cols
        value = matrix[row][col]

        # case 1:
        if value == target:
            return True
        # Case 2:
        elif value < target:
            low = mid + 1
        # Case 3:
        else:
            high = mid - 1
    return False

# Test cases:
array = [4,9,10,13,17,17,19,21]
want = 17
expected = [4,5]

actual = find_start_end(array, want)
print("\n------Example 1------")
print(f"Input: {array}")
print(f"Expected answer: {expected}")
print(f"Actual answer {actual}\n")


# Nested lists: I needed a reference to look at what this would look like and how it works:
# Storing multiple values in lists. Research Computing Summer School. (n.d.). https://openastronomy.org/rcsc18/chapters/03-fundamentals-of-python/03-lists 
test_cases = [
    ("Example 2", [2,4,6,8,10,14,16], 12, [-1,-1]),
    ("Example 3", [], 0, [-1,-1]),
    ("Appears One", [1,3,5,7,9], 5, [2,2]),
    ("At the Start", [2,2,3,4,5], 2, [0,1]),
    ("At the End", [1,2,3,8,8], 8, [3,4]),
    ("All the Same", [3,3,3,3], 3, [0,3]),
    ("Smaller than all", [5,6,7], 1, [-1,-1]),
    ("Larger than all", [5,6,7], 10, [-1,-1]),
    ("Single, Match", [7], 7, [0,0]),
    ("Single, No Match", [7], 3, [-1,-1]),
]


# simplifying the test:
for test, arr, target, expect in test_cases:
    print(f"------{test}------")
    print(f"Input: {arr}")
    print(f"Target: {target}")
    print(f"Expected: {expect}")
    print(f"Actual: {find_start_end(arr, target)}\n")

print("-----Task 2 Tests-----\n")

test_case_2 = [
    ("Example 1", [[1,3,5,7], [10,11,16,20], [23,30,34,60]], 3, True),
    ("Example 2", [[1,3,5,7], [10,11,16,20], [23,30,34,60]], 13, False),
    ("First Element", [[1,3,5,7], [10,11,16,20], [23,30,34,60]], 1, True),
    ("Last Element", [[1,3,5,7], [10,11,16,20], [23,30,34,60]], 60, True),
    ("Start of a Middle Row", [[1,3,5,7], [10,11,16,20], [23,30,34,60]], 10, True),
    ("Smaller Than All", [[1,3,5,7], [10,11,16,20], [23,30,34,60]], 0, False),
    ("Larger Than All", [[1,3,5,7], [10,11,16,20], [23,30,34,60]], 100, False),
    ("Single element, Match", [[5]], 5, True),
    ("Single Element, No Match", [[5]], 2, False),
    ("Single Row", [[1,2,3,4]], 3, True),
    ("Single Column", [[1],[4],[9]], 4, True),
    ("Empty Matrix", [], 1, False),
    ("Empty Row", [[]], 1, False),
]

# Simplifying Test 2:
for m_test, matrix, m_target, flag in test_case_2:
    print(f"-------{m_test}------")
    print(f"Matrix: {matrix}")
    print(f"Target: {m_target}")
    print(f"Expected Flag: {flag}")
    print(f"Actual: {target_in_matrix(matrix, m_target)}\n")




