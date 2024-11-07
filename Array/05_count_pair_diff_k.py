# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/


"""
The problem is to count pairs of indices (i, j) where the absolute difference between nums[i] and nums[j] is equal to k. Instead of using a brute-force approach, we use a hash map (hmap) to track the frequency of each number as we iterate through the list. For each number num, we check if the values num + k and num - k exist in the hash map. If they do, it means that the difference between the current number and the previously seen numbers is exactly k. We then update the result (res) by adding the frequency of those numbers. After processing each number, we update its frequency in the hash map.

Time Complexity: O(n)
Space Complexity: O(n)
"""


from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # Initialize a hash map to store the frequency of each number
        hmap = {}

        # Initialize 'res' to count the number of valid pairs
        res = 0

        # Loop through each number in the list 'nums'
        for num in nums:

            # Add the number of times (num + k) and (num - k) have been seen to 'res'
            # These represent pairs where the absolute difference is 'k'
            res += hmap.get(num + k, 0) + hmap.get(num - k, 0)

            # Update the frequency of the current number 'num' in the hash map
            hmap[num] = hmap.get(num, 0) + 1

        # Return the final count of pairs with absolute difference 'k'
        return res
