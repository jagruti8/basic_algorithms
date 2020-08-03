# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 08:00:12 2020

@author: JAGRUTI
"""

import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    # return None if list is empty
    if len(ints) == 0:
        print("Minimum: {}, Maximum: {}".format(None, None))
        return (None, None)
    
    minimum = ints[0]
    maximum = ints[0]
    index = 1
    
    while(index<len(ints)):
        
        number = ints[index]
        
        # current number less than minimum than set minimum to current number and continue traversing
        if number<minimum:
            minimum = number
            index += 1
            continue
            
        # current number more than maximum than set maximum to current number
        if number>maximum:
            maximum = number
        
        index += 1
        
    print("Minimum: {}, Maximum: {}".format(minimum, maximum))
    
    return (minimum, maximum)

# Edge Cases
print ("Pass" if ((None, None) == get_min_max([])) else "Fail") # Minimum: None, Maximum: None | Pass

# Normal Cases
print ("Pass" if ((0, 0) == get_min_max([0])) else "Fail") # Minimum: 0, Maximum: 0 | Pass
print ("Pass" if ((15, 15) == get_min_max([15])) else "Fail") # Minimum: 15, Maximum: 15 | Pass

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail") # Minimum: 0, Maximum: 9 | Pass

# Large Lists
l = [i for i in range(0, 10000000)]  
random.shuffle(l)
minimum = min(l)
maximum = max(l)
print("Minimum: {}, Maximum: {}".format(minimum, maximum)) # Minimum: 0, Maximum: 9999999
print ("Pass" if ((minimum, maximum) == get_min_max(l)) else "Fail") # Minimum: 0, Maximum: 9999999 | Pass

print("Great! All Done") # Great! All Done