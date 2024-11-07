# https://leetcode.com/problems/3sum/

"""
The approach is to sort the list first and then use the two-pointer technique to find the triplets. For each number nums[i], we use two pointers (j starting from i+1 and k from the end of the list) to find two numbers such that their sum with nums[i] equals zero. By moving the pointers based on the sum, we can efficiently find all valid triplets. To ensure uniqueness, we skip duplicate numbers during the iteration.

Time Complexity: O(nlogn + n^2)
Space Complexity: O(1)
"""

"""
Can you think of brute force ? Anyway try to do it😅
"""


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the input array to facilitate two-pointer technique
        nums.sort()

        # Initialize the result list to store the valid triplets
        res = []

        # Iterate through the array, fixing one element at a time
        for i in range(len(nums) - 2):

            # Skip duplicate elements to avoid repeating triplets
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            # Set up two pointers, j starts right after i and k starts at the end of the list
            j, k = i + 1, len(nums) - 1

            # Use the two-pointer technique to find two numbers whose sum with nums[i] equals zero
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                # If the sum is less than 0, move the left pointer (j) to the right to increase the sum
                if total < 0:
                    j += 1

                # If the sum is greater than 0, move the right pointer (k) to the left to decrease the sum
                elif total > 0:
                    k -= 1

                # If the sum is zero, we've found a valid triplet
                else:
                    res.append([nums[i], nums[j], nums[k]])

                    # Move both pointers inward and skip duplicates
                    j += 1
                    k -= 1

                    # Skip duplicate values of nums[j] to avoid repeated triplets
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate values of nums[k] to avoid repeated triplets
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        # Return the list of unique triplets
        return res
