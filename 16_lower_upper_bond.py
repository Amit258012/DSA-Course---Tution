# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

"""
The problem asks to find the first and last occurrence of a target value in a sorted array. Since the array is sorted, Binary Search is the ideal approach to efficiently find the target values:

We can perform two separate binary searches:
One to find the first occurrence of the target.
Another to find the last occurrence of the target.

First Occurrence (first function):
Use Binary Search to find the first occurrence of the target.
If nums[mid] == target, record the index res and continue searching the left half (r = mid - 1), to ensure it's the first occurrence.


Last Occurrence (last function):
Use Binary Search to find the last occurrence of the target.
If nums[mid] == target, record the index res and continue searching the right half (l = mid + 1), to ensure it's the last occurrence.

Time Complexity: O(n)
Space Complexity: O(1)
"""

"""
Can you solve it by different way ? Anyway try to do it😅
"""


from typing import List


class Solution:

    # Function to find the first occurrence of target
    def first(self, nums, target):
        n = len(nums)
        l = 0
        r = n - 1
        res = -1

        # Binary search to find the first occurrence
        while l <= r:
            mid = (l + r) // 2

            if target <= nums[mid]:
                # Move left to find the first occurrence
                if nums[mid] == target:
                    res = mid  # Store the possible result
                r = mid - 1
            else:
                l = mid + 1

        return res

    # Function to find the last occurrence of target
    def last(self, nums, target):
        n = len(nums)
        l = 0
        r = n - 1
        res = -1

        # Binary search to find the last occurrence
        while l <= r:
            mid = (l + r) // 2

            if target >= nums[mid]:
                # Move right to find the last occurrence
                if nums[mid] == target:
                    res = mid  # Store the possible result
                l = mid + 1
            else:
                r = mid - 1

        return res

    # Main function to return the range of the target
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Call the helper functions to get first and last occurrence
        f = self.first(nums, target)
        l = self.last(nums, target)

        return [f, l]
