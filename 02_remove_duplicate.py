# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


"""
The problem is about removing duplicates from a sorted list nums in-place. Since the list is already sorted, duplicates will always appear consecutively. By using a pointer ins, we can keep track of the next position to insert a unique element as we iterate through the list. We check if the current element is different from the last unique one (temp). If it is, we place it in the ins position and update temp.

Time Complexity: O(n)
Space Complexity: O(1)
"""


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize 'ins' to track the insertion position for unique elements
        ins = 1

        # Set 'temp' to the first element as a reference for comparison
        temp = nums[0]

        # Loop through the list starting from the second element
        for i in range(1, len(nums)):

            # If the current element is different from 'temp' (previous unique element)
            if nums[i] != temp:

                # Place the current element at the 'ins' position in the list
                nums[ins] = nums[i]

                # Increment 'ins' to move to the next insertion position
                ins += 1

                # Update 'temp' to the current element as the new unique reference
                temp = nums[i]

        # Return the value of 'ins', which represents the number of unique elements
        return ins
