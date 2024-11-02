# https://leetcode.com/problems/car-fleet/

"""
Sort by Position: Sort cars by their starting positions in descending order, so we can process the closest cars to the target first.
Calculate Time to Target: For each car, calculate the time it would take to reach the target (time_to_target = (target - position) / speed).
Merge Fleets: If a car reaches the target no faster than the one directly in front of it (i.e., it catches up or stays behind), it forms a fleet with the front car, and we pop it from stack.
Fleet Count: The number of unique times remaining in the stack indicates the number of car fleets.

Time Complexity: O(nlogn)
Space Complexity: O(n)
"""

""""
Try to dry run with random example. 
"""


from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create pairs of (position, speed) for each car and sort them in descending order by position
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)  # Sort so we start from the car closest to the target

        stack = []  # Stack to store the time each car takes to reach the target

        # Process each car in order of their position from closest to farthest from the target
        for p, s in pairs:
            time_to_target = (
                target - p
            ) / s  # Calculate time for this car to reach the target
            stack.append(time_to_target)  # Push the time onto the stack

            # If the current car reaches the target no faster than the car in front, they form a fleet
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()  # Remove the current car's time as it merges with the fleet in front

        return len(stack)  # The stack size represents the number of distinct fleets
