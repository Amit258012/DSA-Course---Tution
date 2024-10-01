# https://leetcode.com/problems/remove-element/


"""
The function removeElement removes all occurrences of a given value val from the array nums in-place. It uses a pointer i to track the position of elements that should remain in the array. As the loop iterates through each element, if the current element is not equal to val, it is placed at index i, and i is incremented. If the element matches val, it is skipped. Finally, the function returns i, which represents the new length of the modified array.

Time Complexity: O(n)
Space Complexity: O(1)
"""


from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i
