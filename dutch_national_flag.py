# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 07:50:52 2020

@author: JAGRUTI
"""

import random

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # return empty list if list is empty
    if len(input_list) == 0:
        return []
    
    # Three indices are maintained one for 0, one for 2 and one index for traversing. The '0' index 
    # maintains position where next '0' should be inserted and samewise '2' index for keeping track of position 2.
    # By inserting 0 and 2 at the correct positions, 1 will be automatically in the correct position.
    
    # index where next 0 will be inserted
    index_0 = 0
    
    # index where next 2 will be inserted
    index_2 = len(input_list)-1
    
    # current index 
    index = 0
    
    # loop will run until current index is greater than the index for keeping track of position 2 
    while(index<=index_2):
        
        number = input_list[index]
        
        # if current number is 0 swap it with element present at index_0 and increment both the counters
        if number == 0:
            input_list[index] = input_list[index_0]
            input_list[index_0] = number
            index_0 += 1
            index += 1
        # if current number is 2 swap it with element present at index_2 and decrement index_2 position.
        # check the number at present index again
        elif number == 2:
            input_list[index] = input_list[index_2]
            input_list[index_2] = number
            index_2 -= 1
        # if neither 1 or 2 at current index, simply increment it
        else:
            index += 1
            
    return input_list
            

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Edge Cases:
test_function([]) # [] | Pass

# Normal Cases:
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]) # [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2] | Pass
test_function([1, 0, 0, 2, 0]) # [0, 0, 0, 1, 2] | Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2] | Pass

test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2] | Pass

test_function([0]) # [0] | Pass
test_function([1]) # [1] | Pass
test_function([2]) # [2] | Pass
test_function([0, 0]) # [0, 0] | Pass
test_function([1, 1]) # [1, 1] | Pass
test_function([2, 2]) # [2, 2] | Pass
test_function([0, 1, 2]) # [0, 1, 2] | Pass
test_function([2, 1, 0]) # [0, 1, 2] | Pass
test_function([0, 1, 0, 1]) # [0, 0, 1, 1] | Pass
test_function([2, 2, 0]) # [0, 2, 2] | Pass

# Large Lists
list_1 = [0 for i in range(1000000)]
list_2 = [1 for i in range(5000000)]
list_3 = [2 for i in range(7000000)]

final_list = list_1 + list_2 + list_3
#print(final_list)
random.shuffle(final_list)
#print(final_list)
test_function(final_list) # Pass

print("Great! All Done") # Great! All Done