# https://www.geeksforgeeks.org/problems/aggressive-cows/0

"""
The goal is to place
k elements (e.g., cows) in the given stalls such that the minimum distance between any two elements is maximized. This problem can be solved with a binary search approach on the possible distance values.

Binary Search Range: The search range for distances is between 1 and the difference between the farthest and closest stalls (stalls[-1] - stalls[0]).
Check Feasibility with canWePlace: For each midpoint distance, use canWePlace to check if it’s possible to place
k elements such that the minimum distance between them is at least the midpoint.
Adjust the Search:
If placing is possible, increase the minimum distance by moving l to mid + 1 and update res to mid.
If not possible, reduce the maximum distance by moving r to mid - 1.

Time Complexity: O(nlog(max(dist)))
Space Complexity: O(1)
"""


import math
from typing import List


class Solution:
    # Helper function to check if we can place k elements with at least 'dist' distance between them
    def canWePlace(self, stalls, dist, k):
        prev = stalls[0]  # Position of the first placed element
        cnt = 1  # Initial count includes the first placed element

        # Iterate through each stall position
        for stallPos in stalls:
            d = stallPos - prev  # Calculate distance from the previous element
            if d >= dist:  # If distance is at least 'dist'
                cnt += 1  # Place an element
                prev = stallPos  # Update position of last placed element

        return cnt >= k  # Return True if we could place at least k elements

    # Main function to find the largest minimum distance to place k elements in n stalls
    def solve(self, n, k, stalls):
        stalls.sort()  # Sort stall positions to apply binary search
        l = 1  # Minimum possible distance
        r = stalls[-1] - stalls[0]  # Maximum possible distance
        res = -1  # Variable to store the result

        # Binary search to find the largest minimum distance
        while l <= r:
            mid = (l + r) // 2  # Calculate middle distance

            # Check if placing elements with 'mid' distance is feasible
            if self.canWePlace(stalls, mid, k):
                l = mid + 1  # Try for a larger distance
                res = mid  # Update result with current mid
            else:
                r = mid - 1  # Try for a smaller distance

        return res  # Return the largest minimum feasible distance
