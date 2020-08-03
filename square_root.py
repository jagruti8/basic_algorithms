# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 07:29:42 2020

@author: JAGRUTI
"""
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None:
        print("Invalid")
        return
    i = 0   # i to know the no of iterations - time complexity
      
    flag = 0
    # negative number then make the number positive and raise flag to -1
    if number<0:
        flag = -1
        number = -number
    
    # approach similar to binary search
    low = 0
    high = number
    
    while(low<=high):
        
        mid = (low + high) // 2
        i += 1 
        
        # reached the target value
        if mid**2 == number:
            print("No of iterations", i)
            if flag == -1: # number is negative
                return (str(mid)+'i')
            return mid
        
        # discard the upper half
        elif mid**2>number:
            high = mid - 1
            
        # discard the lower half
        else:
            low = mid + 1
            
        mid = (low + high) // 2
        
    print("No of iterations", i)
    
    # floor value for 2.5 = 2
    # floor value for -2.5 = -3. hence (mid + 1) is returned
    if flag == -1:
        return (str(mid+1)+'i')
    return mid

# The expected time complexity is O(log(n))

# Edge Case:
print(sqrt(None))  # Invalid None

# Normal cases for both positive and negative numbers
print ("Pass" if  (3 == sqrt(9)) else "Fail")  # Pass  --- No of iterations 4
print ("Pass" if  ('3i' == sqrt(-9)) else "Fail")   # Pass  --- No of iterations 4
print ("Pass" if  (4 == sqrt(16)) else "Fail")  # Pass  --- No of iterations 4
print ("Pass" if  ('4i' == sqrt(-16)) else "Fail")   # Pass  --- No of iterations 4
print ("Pass" if  (5 == sqrt(27)) else "Fail")   # Pass  --- No of iterations 5
print ("Pass" if  ('6i' == sqrt(-27)) else "Fail")   # Pass  --- No of iterations 5
print ("Pass" if  (0 == sqrt(0)) else "Fail")   # Pass  --- No of iterations 1
print ("Pass" if  (1 == sqrt(1)) else "Fail")  # Pass  --- No of iterations 2
print ("Pass" if  ('1i' == sqrt(-1)) else "Fail")  # Pass  --- No of iterations 2
print ("Pass" if  (100 == sqrt(10099)) else "Fail")      # Pass  --- No of iterations 14
print ("Pass" if  ('101i' == sqrt(-10099)) else "Fail")   # Pass  --- No of iterations 14
  
# Very large numbers
print ("Pass" if  (15811 == sqrt(250000063)) else "Fail")    # Pass  --- No of iterations 28
print ("Pass" if  ('15812i' == sqrt(-250000063)) else "Fail")   # Pass  --- No of iterations 28
