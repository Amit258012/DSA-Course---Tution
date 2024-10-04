# https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1

"""
 we can traverse the array from right to left, keeping track of the maximum element (right_most) seen so far. If the current element is greater than or equal to this maximum, it is a leader, and we add it to the result list. After traversing the array, we reverse the result to maintain the correct order.

Time Complexity: O(n)
Space Complexity: O(n)
"""

"""
Can you solve by looping forward ? Anyway try to do it😅
"""


from typing import List


class Solution:
    # Function to find the leaders in the array.
    def leaders(self, n, arr):
        # Initialize an empty list to store the leaders
        res = []

        # Initialize the rightmost element as the last element in the array
        right_most = arr[-1]

        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            # If the current element is greater than or equal to the rightmost element,
            # it is a leader, so add it to the result list
            if arr[i] >= right_most:
                res.append(arr[i])
                # Update the right_most element to the current one
                right_most = arr[i]

        # Reverse the result list to maintain the order of leaders as in the original array
        return res[::-1]
