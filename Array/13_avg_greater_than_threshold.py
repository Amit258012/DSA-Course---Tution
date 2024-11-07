# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

"""
We use a sliding window technique to maintain the sum of k consecutive elements at all times.
Initially, we sum up the first k-1 elements, then for every new element in the array starting from k-1, we add it to the current window and check the average.
After checking the average, we subtract the element that moves out of the window (from the left side) and repeat this for the entire array.
If the average of a window is greater than or equal to the threshold, we increment the count.

Time Complexity: O(n)
Space Complexity: O(1)
"""

"""
Can you solve it by different way ? Anyway try to do it😅
"""


from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        valid_subarray_count = 0

        n = len(arr)  # Length of the input array
        window_sum = 0  # To maintain the sum of the current window of size k

        # First, calculate the sum of the first k-1 elements to set up the sliding window
        for i in range(k - 1):
            window_sum += arr[i]

        # Now, process the entire array with a sliding window approach
        for i in range(k - 1, n):
            window_sum += arr[i]  # Add the next element to the current window
            window_avg = window_sum / k  # Calculate the average of the current window

            # If the average is greater than or equal to the threshold, increment the count
            if window_avg >= threshold:
                valid_subarray_count += 1

            # Slide the window: remove the element that is moving out of the window
            window_sum -= arr[i - k + 1]

        return valid_subarray_count
