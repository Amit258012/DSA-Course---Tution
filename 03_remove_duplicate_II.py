# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/


"""
The goal is to remove duplicates from a sorted list, allowing each element to appear at most twice. The key idea is to use an index i to track the position where the next valid element (an element that does not violate the "at most twice" condition) should be placed. We iterate through the list and for each element, if the element at index i-2 is not equal to the current element n, we place n at index i and move the i pointer forward.

Time Complexity: O(n)
Space Complexity: O(1)
"""


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize 'i' to keep track of the next valid position for a unique element
        i = 0

        # Loop through each element 'n' in the list 'nums'
        for n in nums:

            # If 'i' is less than 2, or if the current element 'n' is not equal to the element at 'i-2',
            # then we can place 'n' at the 'i' position (i.e., allowing up to 2 duplicates).
            if i < 2 or n != nums[i - 2]:

                # Place the current element 'n' at index 'i'
                nums[i] = n

                # Move the 'i' pointer forward
                i += 1

        # Return 'i' which represents the new length of the list with at most 2 duplicates allowed
        return i
