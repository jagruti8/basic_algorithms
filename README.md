# basic_algorithms
A handful of basic search and sort algorithms

# requirements:
python3

# Square_Root:
Finding the square root of the integer without using any Python library.
For integers which are not proper square, have to find out the floor value of the square root.
The expected time complexity is O(log(n)).

Analysis:
1. For finding square root of the number with O(log(n)) time complexity, binary search procedure has been applied. 
2. For calculating square root of negative integers, they are first mutiplied by '-1' so as to treat them as positive integers
   and then calculate their square root and in return step add a 'i'. Also, for negative integers, those are proper square, 
   the approach is similar, however, for negative numbers which are not a proper square, '1' is added to the answer since floor(-2.5) = -3 
   whereas floor(2.5) = 2. As seen from the number of iterations, O(log(n)) is the time complexity. 
3. Since, only temporary variables like 'i', 'flag', 'low', 'mid' and 'high' are used, it has O(1) space complexity

# Rotated_Array_Search:
Find an element in a sorted array which is rotated at some random pivot point.
Assumption: There are no duplicates in the array 
Expectation: Algorithm's runtime complexity must be in the order of O(log n).

Analysis:
The approach is similar to binary search with only slight modifications:
1. If array is already sorted, the program control goes to sorted_array search. The idea for not handling it in the same function is because, 
   the search procedure for rotated search array has more number of comparisons, which is avoided by transferring the control.
2. If array's first half is sorted and target is present in first half, control goes to normal binary search for sorted array for
   the first half. If target is not present in first half, second half is considered.
3. If array's second half is sorted and target is present in second half, control goes to normal binary search for sorted array for
   the second half. If target is not present in second half, first half is considered.
4. The above steps are repeated as per the conditions until the target is reached or lower_index exceeds the upper_index.

The worst-case time complexity is O(log(n)) [Binary search]
The space complexity is O(1) (Auxiliary space) [Iterative method]

# Rearrange_Array_Elements:
Rearrange Array Elements so as to form two number such that their sum is maximum. 
Return these two numbers. 
Assumption: All array elements are in the range [0, 9]. 
Requirements: The number of digits in both the numbers cannot differ by more than 1. No in-built sorting function to be used.
Expectation: Time complexity is O(nlog(n)).

Analysis:
The array is first sorted using randomized quick sort - recursive tail approach due to the following reasons:

1. Faster than heapsort
2. In-place sorting hence better than merge sort
3. Worst-case time complexity is O(n^2), but chances are less incase of randomized quicksort. 
4. Best and average case time complexity is O(nlog(n))
5. By following recursive tail approach [Idea from "https://www.geeksforgeeks.org/"], worst-case space complexity 
   is reduced from O(n) to O(log(n)). 

After sorting, since only one digit elements from 0-9 are present, the numbers are made by alternately joining digits 
from the odd and even positions for the first and second number respectively, as this is the way the sum will be maximum.
This is done using a single traversal of the sorted array, hence time complexity is O(n).
However, the numbers are made by first concatenating as a string, hence space complexity is number of digits in both the numbers which is equal to the number of elements in the array ,i.e, O(n).

Hence, overall expected time complexity is O(nlog(n)) governed by the sorting technique and space complexity is O(n) due to storing numbers as strings.

# Dutch_National_Flag_Problem:
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
Requiremnets: No in-built sorting function to be used.

Analysis:
1. The idea is 0's should be put first, then 1's and 2's. 
2. Since sorting needs single traversal, hence, by placing 0's at the left side and 2's at the right side of the array, 
   1's would be automatically in the corect position.
3. Hence, 3 counters are needed, one for keeping track of 0's, one for 2's and the one for traversing and checking the elements. 
4. If we encounter a '0', swap it with the element at index_0 position and increment both the counters.
5. Hence this way our 0's will be pushed to the left of the array.
6. Then, if a '2' is encountered, swap it with the element at index_2 position, but this time only decrement index_2 counter.
7. The current index stays there and checks the swapped element and act accordingly.
8. This way 2's are pushed to the right side of the array.
9. If 1 is encountered, simply the traversal counter is incremented as 1's position is automatically adjusted. 

The worst-case time complexity is O(n).
The space complexity is O(1)(auxiliary) since the sorting takes place in-sort and is iterative.

# Autocomplete_with_trie:
Implement the autocomplete feature of Google search using Tries

Analysis:
1. Insertion: Time Complexity: O(n) where n is the number of characters in the word. 
   Even if some characters exists, we have to traverse all the characters starting from the first letter. 
   Each character represents a node.
   Worst-Case Space Complexity arises when no letter of the word is present. 
   Hence one node each for one character where each node stores a character, a boolean value 
   and a list of size 26 for the child node indexes - O(26 * n) = O(n)
2. Finding: Best Case Time Complexity is O(1), when the word is not present and worst-case time complexity is O(n) when the word is present.
   Since iterative approach is used, hence space complexity is O(1)
3. Suffixes: Worst Case Time Complexity when prefix is "", means all the nodes in the trie. 
   Suppose each node except leaf nodes has 26 children and n(starting from 1) is the depth of trie, 
   then maximum traversal is the number of nodes which is (((26^n)-1)/(26-1)). 
   Best case is when prefix does not exist or prefix is a whole word whose last node does not have any children. 
   Space complexity is due to recursion and worst-case is O(n) where n(starting from 1) is the depth of the tree and hence represents the recursion depth.

# Max_Min_Unsorted_Array:
Finding the maximuma and minimum integer in an unsorted array in a single traversal.

Analysis:
1. The above algorithm has a time complexity of O(n) and space complexity of O(1). 
2. If element is already small than minimum, it means it can't be more than maximum, hence continue traversal
   without checking the maximum condition, thus lessening one comparison. 
3. This task is also accomplished in a single traversal. 
4. However, the maximum number of comparisons take place when the array is already sorted(2(n-1) times) 
   and minimum when the array is reverse sorted((n-1) times) [n is the no of elements in the array].
   
# Request_Routing:
Building a HTTP Router using a Trie

Analysis:
1. Dictionary is implemented as the data structure for the nodes' children because of constant look-up property.

2. For insertion and finding a path, first splitting of the path(no of parts separated by '/') takes place. 
   Hence, if path is m characters long, time complexity for splitting is O(m) as traversing through the path is required. 
   Then after splitting suppose we get n parts (where n<=m). 
   Then, for both inserting and finding, we need to check if the path_part exists in the dictionary which has
   an average-case time complexity of O(1) [worst-case time-complexity for dictionary lookup is O(n), but chances are less]. 
   Then for traversing the entire path-parts, n iterations are required for insertion and worst-case n iterations are required for finding. 
   This means this has a time-complexity of O(n). Hence, the time complexity is dominated by splitting which is O(m) for both insertion as well as finding

3. Space complexity : Suppose we have k different paths for each node, and maximum depth of trie is n(starts from 1). 
   For each node, we have to store two strings: the path name(suppose c characters) and the handler name(suppose h characters).
   Hence, worst case space complexity is O(((k^n)-1)/(k-1)(c+h)) for the entire Trie.
