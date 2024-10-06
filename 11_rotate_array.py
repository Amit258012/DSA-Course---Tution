# https://leetcode.com/problems/rotate-array/description/

"""
The goal is to rotate the array nums to the right by k steps. Instead of using extra space or shifting elements one by one, we can solve this problem in-place using the reverse method. The idea is to reverse the entire array, then reverse the first k elements, and finally reverse the remaining elements. This ensures that the elements are placed in their correct rotated positions.

Time Complexity: O(n)
Space Complexity: O(1)
"""

"""
Can you solve it by different way ? Anyway try to do it😅
"""


from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Helper function to reverse elements between indices l and r
        def reverseNow(l, r, nums):
            left = l
            right = r

            # Swap elements from the two ends and move towards the middle
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Get the length of the array
        n = len(nums)

        # If k is larger than n, we take k modulo n to reduce the rotation
        k %= n

        # Step 1: Reverse the entire array
        reverseNow(0, n - 1, nums)

        # Step 2: Reverse the first k elements
        reverseNow(0, k - 1, nums)

        # Step 3: Reverse the rest of the array from index k to the end
        reverseNow(k, n - 1, nums)
