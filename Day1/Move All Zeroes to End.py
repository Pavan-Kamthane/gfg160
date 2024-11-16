'''
Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. Do the mentioned change in the array in place.

Examples:

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.
Input: arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.
Input: arr[] = [0, 0]
Output: [0, 0]
Explanation: No change in array as there are all 0s.
Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 105
'''

class Solution:
    def pushZerosToEnd(self, arr):
        # This pointer tracks where the next non-zero element should go
        non_zero_index = 0
        
        # Loop through the array
        for i in range(len(arr)):
            if arr[i] != 0:  # If it's a non-zero element
                # Store the current element in a temporary variable
                temp = arr[i]
                
                # Move the element at non_zero_index to the current position
                arr[i] = arr[non_zero_index]
                
                # Assign the original non-zero element to the correct spot
                arr[non_zero_index] = temp
                
                # Move the pointer to the next spot for non-zero elements
                non_zero_index += 1
                
        return arr