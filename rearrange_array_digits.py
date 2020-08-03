# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 07:45:36 2020

@author: JAGRUTI
"""

import random

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    Assumption: All array elements are in the range [0, 9]
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # sum is 0 if there are no elements
    if len(input_list) == 0:
        print("Numbers are:", 0, 0)
        return [0, 0]
    
    # sum is the only element present in the list
    if len(input_list) == 1:
        print("Numbers are:", input_list[0], 0)
        return [input_list[0], 0]
    
    # sort the list using randomized quick sort - O(nlog(n)) - Best and average case time complexity
    sorted_list = quick_sort(input_list, 0, len(input_list)-1)
    
    index = 0
    num_1 = ''
    num_2 = ''
    
    # join numbers alternately from odd and even positions for first and second number respectively
    while(index<len(sorted_list)):
        num_1 = str(sorted_list[index]) + str(num_1)  
        
        # check if digit at even position exists
        if (index + 1)<len(sorted_list):
            num_2 = str(sorted_list[index+1]) + str(num_2) 
        
        index += 2
        
    print("Numbers are:" ,int(num_1), int(num_2))
    return [int(num_1), int(num_2)]

# quick sort for sorting the array - tail recursive approach to have worst case time complexity of O(log(n)) - Idea from 
# "https://www.geeksforgeeks.org/"
    
def quick_sort(array, low, high):
    
    while(low<high):
         
        pivot_index = sort_again(array, low, high)
        
        quick_sort(array, low, pivot_index-1)
    
        low = pivot_index + 1
        
    return array
    
def sort_again(array, low, high):
    
    # pick random element as pivot - randomized quick sort to have less chances of worst-case scenario - time complexity - O(n^2)
    randpivot = random.randrange(low, high) 
    
    # swap pivot value with the highest index value
    swap(array, randpivot, high)

    left_index = low
    pivot_index = high
    
    # until pivot element reaches its correct position in the array - left-side elements smaller than equal to pivot and 
    # right-side elements larger than pivot
    while(left_index!=pivot_index):
        
        if array[left_index]<=array[pivot_index]:
            left_index += 1
            continue
        # fill left_index position with the element to the left of pivot, shift pivot element to left and
        # get the left_index element to pivot position. Decrement the pivot index
        swap(array, left_index, pivot_index-1)
        swap(array, pivot_index, pivot_index-1)
        pivot_index -= 1
        
    return pivot_index
    
# function for swapping two elements
def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp
        
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    output_sum = sum(output)
    solution_sum = sum(solution)
    print("My solution: {}, Target: {}".format(output_sum, solution_sum))
    if output_sum == solution_sum:
        print("Pass")
    else:
        print("Fail")

# Edge cases
test_function([[], [0, 0]]) # Numbers are: 0 0 | My solution: 0, Target: 0 | Pass
test_function([[0], [0, 0]]) # Numbers are: 0 0 | My solution: 0, Target: 0 | Pass
test_function([[1], [1, 0]]) # Numbers are: 1 0 | My solution: 1, Target: 1 | Pass

# Normal cases
test_function([[1, 2, 3, 4, 5], [542, 31]]) # Numbers are: 531 42 | My solution: 573, Target: 573 | Pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]]) # Numbers are: 852 964 | My solution: 1816, Target: 1816 | Pass

# Large Lists
final_list = []
for i in range(10):
    final_list += [i for j in range(i+1)]
#print(final_list)
random.shuffle(final_list)
#print(final_list)
num1 = 9999988888777766655544433210
num2 = 999998888777766665554433221
test_function([final_list, [num1, num2]])
# Numbers are: 9999988888777766655544433210 999998888777766665554433221
# My solution: 10999987777555533321098866431, Target: 10999987777555533321098866431
# Pass