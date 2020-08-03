# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 07:38:28 2020

@author: JAGRUTI
"""

# You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n)

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # return if list is empty
    if len(input_list) == 0:
        return -1
    
    low = 0
    high = len(input_list)-1
    
    while(low<=high):
        
        # if array is sorted
        if input_list[low] <= input_list[high]:
            index = sorted_array(input_list, low, high, number)
            return index
            
        mid = (low + high) // 2
        
        # if target is reached
        if input_list[mid] == number:
            return mid
    
        # if array first half is sorted
        if input_list[low] <= input_list[mid]:
            
            # if target is present in first half, search in first half
            if number>=input_list[low] and number<=input_list[mid]:
                high = mid - 1
                index = sorted_array(input_list, low, high, number)
                return index
            # search in second half
            else:
                low = mid + 1
        
        # if array second half is sorted
        elif input_list[mid] <= input_list[high]:
            
            # if target is present in second half, search in second half
            if number>=input_list[mid] and number<=input_list[high]:
                low = mid + 1
                index = sorted_array(input_list, low, high, number)
                return index
            # search in first half
            else:
                high = mid - 1
        
    # if target is not present
    return -1

# binary search for sorted array
def sorted_array(input_list, low, high, number):
    
    while(low<=high):
        
        mid = (low + high) // 2
        # if target is reached
        if input_list[mid] == number:
            return mid
        # consider first half
        elif number < input_list[mid]:
            high = mid - 1
        # consider second half
        else:
            low = mid + 1
    return -1
        
# linear seach for comparison to our approach
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    linear_search_result = linear_search(input_list, number)
    rotated_array_search_result = rotated_array_search(input_list, number)
    print("Linear Search Result: {}, My Program Result: {}".format(linear_search_result, rotated_array_search_result))
    if linear_search_result == rotated_array_search_result:
        print("Pass")
    else:
        print("Fail")

#Time Complexity - O(log(n))

# Edge Case
test_function([[], 4]) # Linear Search Result: -1, My Program Result: -1, Pass
        
# Normal Cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])  # Linear Search Result: 0, My Program Result: 0, Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])  # Linear Search Result: 5, My Program Result: 5, Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])  # Linear Search Result: 2, My Program Result: 2, Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1]) # Linear Search Result: 3, My Program Result: 3, Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) # Linear Search Result: -1, My Program Result: -1, Pass
test_function([[6, 7, 8, 1, 2, 3, 4], -2]) # Linear Search Result: -1, My Program Result: -1, Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 4]) # Linear Search Result: 6, My Program Result: 6, Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 3]) # Linear Search Result: 5, My Program Result: 5, Pass

# Sorted
test_function([[1, 2, 3, 4, 6, 7, 8], 2]) # Linear Search Result: 1, My Program Result: 1, Pass

# Large Lists
integers = list(range(0,100000000,2))
integers1 = [None for i in range(len(integers))]
integers1[:42] = integers[len(integers)-42:]
integers1[42:] = integers[:len(integers)-42]
test_function([integers1, 99999998]) # Linear Search Result: 41, My Program Result: 41, Pass
test_function([integers1, 100000000]) # Linear Search Result: -1, My Program Result: -1, Pass

print("All Done! Great Job") # All Done! Great Job
