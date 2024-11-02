# https://leetcode.com/problems/daily-temperatures/

"""
Stack Storage: The stack stores pairs of [temperature, index] to keep track of temperatures that haven’t yet found a warmer day.
Check for Warmer Days:
For each temperature, if it’s warmer than the temperature on top of the stack, pop the stack and calculate the difference in days (i - stackIdx).
Update res[stackIdx] with the number of days until this warmer temperature.
Push Current Day: After processing warmer temperatures, push the current day’s temperature and index onto the stack to find a future warmer day for it.

Time Complexity: O(n)
Space Complexity: O(n)
"""

""""
Try to dry run with random example. 
"""


from typing import List


class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)  # Length of the temperature list
        res = [0] * n  # Initialize result list with all zeroes
        stack = []  # Stack to store [temperature, index] pairs

        # Iterate through each temperature along with its index
        for i, t in enumerate(temp):
            # Check if the current temperature is higher than the temperature at the top of the stack
            while stack and t > stack[-1][0]:
                stackTemp, stackIdx = (
                    stack.pop()
                )  # Pop the last temperature and index from the stack
                res[stackIdx] = (
                    i - stackIdx
                )  # Calculate the number of days until a warmer temperature
            # Push the current temperature and its index onto the stack
            stack.append([t, i])

        return res  # Return the result list
