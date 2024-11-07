# https://leetcode.com/problems/move-zeroes/

"""
 We maintain two pointers, slow and fast. The fast pointer iterates over the array, and whenever a non-zero element is found at fast, we swap it with the element at the slow pointer (if the element at slow is zero). The slow pointer is used to track where the next non-zero element should be placed.

Time Complexity: O(n)
Space Complexity: O(1)
"""

"""
Can you solve it by different way ? Anyway try to do it😅
"""


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize slow pointer to track the position of zeroes
        slow = 0

        # Iterate over the array with the fast pointer
        for fast in range(len(nums)):

            # If the current element at slow is zero and fast points to a non-zero element, swap them
            if nums[slow] == 0 and nums[fast] != 0:
                # Swap the zero at 'slow' with the non-zero element at 'fast'
                nums[slow], nums[fast] = nums[fast], nums[slow]
                # Increment slow pointer after swap
                slow += 1

            # If the current element at slow is non-zero, move slow pointer ahead
            if nums[slow] != 0:
                slow += 1
