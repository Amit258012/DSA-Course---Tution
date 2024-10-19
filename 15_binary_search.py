"""
Binary Search is an efficient algorithm used to find the position of a target value within a sorted array. The idea is to repeatedly divide the search interval in half:

Start with the entire array.
Compare the target value with the middle element.
If the target is equal to the middle element, you've found the target.
If the target is smaller than the middle element, repeat the process with the left half of the array.
If the target is larger than the middle element, repeat the process with the right half of the array.
The process continues until the search interval becomes empty, meaning the target is not present in the array.
Why Binary Search is efficient: Instead of checking each element sequentially, Binary Search eliminates half of the remaining elements with each step. This leads to a logarithmic time complexity.

Time Complexity: O(logn)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        # Initialize the left and right pointers for the search space
        left, right = 0, len(nums) - 1

        # Continue searching while there is a valid range
        while left <= right:
            # Calculate the middle index
            mid = left + (right - left) // 2

            # Check if the target is at the middle index
            if nums[mid] == target:
                return mid  # Target found, return its index
            elif nums[mid] < target:
                # If target is greater, ignore the left half
                left = mid + 1
            else:
                # If target is smaller, ignore the right half
                right = mid - 1

        # If target is not found, return -1
        return -1
