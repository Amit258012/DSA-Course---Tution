# https://leetcode.com/problems/two-sum/


"""
Brute-force approach
The problem requires finding two distinct indices i and j such that the sum of nums[i] and nums[j] equals the target. The solution uses a brute-force approach by checking every possible pair of numbers to see if their sum matches the target. We use two nested loops: the outer loop fixes the first number, and the inner loop checks all the numbers after the fixed one to find a valid pair.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Get the length of the input list 'nums'
        n = len(nums)

        # Outer loop to iterate through the list (fix the first number)
        for i in range(n - 1):

            # Inner loop to check all the numbers after the fixed one
            for j in range(i + 1, n):

                # If the sum of nums[i] and nums[j] equals the target, return their indices
                if nums[i] + nums[j] == target:
                    return [i, j]


"""
Optimal approach
As we iterate through the list, for each number num, we calculate the required complement (target - num) that would sum up to the target. If the complement already exists in the hash map, we return the indices of the current number and the complement. If not, we add the current number and its index to the hash map.

Time Complexity: O(n)
Space Complexity: O(n)
"""


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize a hash map to store the numbers and their corresponding indices
        hmap = {}  # {num: idx}

        # Loop through the list, using 'i' as the index and 'num' as the current number
        for i, num in enumerate(nums):

            # Calculate the required complement to reach the target
            req = target - num

            # Check if the required complement is already in the hash map
            if req in hmap:
                # If it is, return the index of the current number and the complement
                return [i, hmap[req]]

            # Otherwise, store the current number and its index in the hash map
            else:
                hmap[num] = i
