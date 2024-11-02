# https://leetcode.com/problems/search-in-rotated-sorted-array/

"""
The problem involves searching for a target in a rotated sorted array, which means the array was originally sorted but has been rotated at an unknown pivot. To solve this efficiently, binary search is used by taking advantage of the sorted halves.

We perform a binary search by calculating the middle element.
If the middle element matches the target, we return its index.
If the left half of the current search range is sorted, we check if the target lies within this sorted half:
If it does, adjust the right pointer to narrow the search to this half.
Otherwise, adjust the left pointer to continue searching in the unsorted right half.
Similarly, if the right half is sorted, we check if the target lies within this sorted half and adjust pointers accordingly.
If the target is not found after narrowing down the search range, return -1.

Time Complexity: O(logn)
Space Complexity: O(1)
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        # Begin binary search loop
        while l <= r:
            # Calculate mid-point of the current search range
            mid = (l + r) // 2

            # Check if the middle element is the target
            if nums[mid] == target:
                return mid

            # Check if the left side of the array is sorted
            if nums[l] <= nums[mid]:
                # If the target is within the sorted left half
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1  # Narrow the search to the left half
                else:
                    l = mid + 1  # Narrow the search to the right half

            # Check if the right side of the array is sorted
            if nums[mid] <= nums[r]:
                # If the target is within the sorted right half
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1  # Narrow the search to the right half
                else:
                    r = mid - 1  # Narrow the search to the left half

        # Return -1 if target is not found
        return -1
