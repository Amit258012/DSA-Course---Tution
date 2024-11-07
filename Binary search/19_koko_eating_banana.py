# https://leetcode.com/problems/koko-eating-bananas/description/

"""
The goal is to find the minimum integer speed k at which a person can eat all piles of bananas within 
h hours. This is a binary search problem on the speed range, where for each speed 
k we calculate the total hours required to finish all piles. By adjusting 
k based on whether the hours are within or exceed 
h, we can efficiently find the minimum feasible eating speed.

Binary Search Range: Start with the speed range from 1 to the largest pile, as the speed must be between these limits.
Calculate Hours for Each Speed: For a given speed 
k, calculate the total hours needed using calcTotalHr.
Adjust the Search:
If the hours are within 
h, try a smaller speed by decreasing high to check if there’s a lower possible eating speed.
If the hours exceed 
h, increase low to try a higher speed.

Time Complexity: O(nlog(max(piles)))
Space Complexity: O(1)
"""


import math
from typing import List


class Solution:
    # Helper function to calculate the total hours needed to finish all piles at a given speed k
    def calcTotalHr(self, piles, k):
        n = len(piles)
        totalHr = 0

        # Calculate hours needed for each pile and sum them up
        for i in range(n):
            totalHr += math.ceil(
                piles[i] / k
            )  # Divide each pile by k and take the ceiling

        return totalHr

    # Main function to find the minimum eating speed to finish all piles within h hours
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = max(piles)  # Find the maximum pile size for the upper limit of speed

        # Initialize binary search range
        low = 1
        high = maxi

        # Perform binary search to find the minimum speed
        while low <= high:
            mid = (low + high) // 2  # Calculate middle speed
            totalhr = self.calcTotalHr(
                piles, mid
            )  # Calculate hours required at mid speed

            # Check if hours are within the allowed limit
            if totalhr <= h:
                high = mid - 1  # Try a smaller speed
            else:
                low = mid + 1  # Try a larger speed

        return low  # Minimum feasible eating speed
