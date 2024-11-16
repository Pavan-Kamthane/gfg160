'''
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.
Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.
Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105
'''

class Solution:
    def getSecondLargest(self, arr):
        # Step 1: Get the largest element
        maxElem = self.getMax(arr)
        
        # Step 2: Remove all occurrences of the largest element
        arr = self.remove_items(arr, maxElem)
        
        # Step 3: If there's no second largest element (i.e., array is empty now)
        if len(arr) == 0:
            return -1
        
        return self.getMax(arr)
    
    def getMax(self, arr):
        maxi = arr[0]
        for i in arr:
            if i > maxi:
                maxi = i
        return maxi
    
    def remove_items(self, arr, item):
        # yat all occrance delet krych
        return [x for x in arr if x != item]