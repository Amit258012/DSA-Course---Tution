# https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1

"""
Binary Search (first method): This method is used to find the first occurrence of a target (1) in a sorted row. Using binary search here helps in reducing the search time from linear to logarithmic.

Finding the Row with Maximum 1's (rowWithMax1s method): This method iterates over each row in the matrix and finds the count of 1's. It updates the row index (res) if the current row has more 1's than the previously recorded maximum.

Time Complexity: O(nlogn)
Space Complexity: O(1)
"""


from typing import List


class Solution:
    def first(self, nums, target):
        n = len(nums)
        l = 0
        r = n - 1
        res = -1

        # Perform binary search to find the first occurrence of 'target' in 'nums'
        while l <= r:
            mid = (l + r) // 2

            # If 'target' is less than or equal to 'nums[mid]', move the right pointer left
            if target <= nums[mid]:
                if nums[mid] == target:
                    res = mid  # Update 'res' if 'target' is found
                r = mid - 1  # Continue search in the left half
            else:
                l = mid + 1  # Move left pointer right if 'target' is greater

        return res

    def rowWithMax1s(self, arr):
        res = -1  # Result to store the index of row with max 1's
        max_1 = 0  # Variable to track the maximum count of 1's found in any row
        rows = len(arr)
        cols = len(arr[0])

        # Iterate over each row in the matrix
        for i, row in enumerate(arr):
            # Find the first occurrence of 1 in the current row using the helper function 'first'
            fa = self.first(row, 1)
            # If a 1 is found and the count of 1's in this row is greater than the previous maximum,
            # update 'max_1' and the result 'res' with the current row index
            if fa != -1:
                if max_1 < (cols - fa):  # Calculate the count of 1's in the row
                    max_1 = cols - fa
                    res = i

        return res
