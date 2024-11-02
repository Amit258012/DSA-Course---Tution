# https://leetcode.com/problems/valid-parentheses/

"""
Push Expected Closings for Openings: When encountering an opening bracket, push its corresponding closing bracket onto the stack.
Check Closings for Matches: For each closing bracket, pop the top of the stack (expected closing bracket) and check if it matches. If it doesn’t, or if the stack is empty when trying to pop, it’s invalid.
Stack Should Be Empty at End: After iterating, the stack should be empty if all brackets matched correctly.

Time Complexity: O(n)
Space Complexity: O(n)
"""


from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Initialize an empty stack to store expected closing brackets

        # Iterate over each character in the string
        for ch in s:
            # If the character is an opening bracket, push the corresponding closing bracket to the stack
            if ch in "({[":
                if ch == "(":
                    stack.append(")")
                elif ch == "{":
                    stack.append("}")
                elif ch == "[":
                    stack.append("]")

            # If it's a closing bracket, pop from the stack and check for a match
            else:
                if len(stack) == 0:  # If stack is empty, no matching opening bracket
                    return False
                cb = stack.pop()  # Pop the expected closing bracket from the stack
                if (
                    ch != cb
                ):  # If it doesn't match the current closing bracket, return False
                    return False

        # If the stack is empty, all brackets were matched correctly
        return len(stack) == 0
