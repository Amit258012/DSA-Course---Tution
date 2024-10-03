# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


"""
We initialize two pointers: one at the beginning (l) and one at the end (r) of the list. If the sum of the elements at these pointers equals the target, we return their indices. If the sum is greater than the target, we move the right pointer (r) to the left to reduce the sum. If the sum is less than the target, we move the left pointer (l) to the right to increase the sum. This process continues until we find the pair.

Time Complexity: O(n)
Space Complexity: O(1)
"""


from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers: 'l' starting from the left and 'r' from the right
        l, r = 0, len(numbers) - 1

        # Continue the loop while 'l' is less than 'r'
        while l < r:

            # If the sum of the elements at 'l' and 'r' equals the target, return their 1-based indices
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]  # Adding 1 to convert 0-based to 1-based index

            # If the sum is greater than the target, move the right pointer to the left to reduce the sum
            elif numbers[l] + numbers[r] > target:
                r -= 1

            # If the sum is less than the target, move the left pointer to the right to increase the sum
            else:
                l += 1
