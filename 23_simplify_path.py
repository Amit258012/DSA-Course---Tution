# https://leetcode.com/problems/simplify-path/

"""
Accumulate Directory/File Names: As we go through each character, accumulate characters in cur until we encounter a /, which marks the end of a directory name.
Handle Directory Navigation:
"..": Go up one directory, so pop the last element from stack if it’s not empty.
".": Represents the current directory, so it’s ignored.
Valid Directory Names: If cur is a valid name, push it to stack.
Build Simplified Path: Join all elements in stack with / to form the simplified path.

Time Complexity: O(n)
Space Complexity: O(n)
"""

""""
Try to dry run with random example. 
"""


from typing import List


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []  # Initialize a stack to store valid directory names
        cur = (
            ""  # Variable to accumulate characters for the current directory/file name
        )

        # Iterate through each character in the path with an added "/" to ensure the last directory is processed
        for ch in path + "/":
            if (
                ch == "/"
            ):  # If we encounter a "/", process the accumulated directory/file name in `cur`
                if (
                    cur == ".."
                ):  # ".." means to go up one directory, so pop from stack if not empty
                    if stack:
                        stack.pop()
                elif (
                    cur != "" and cur != "."
                ):  # If `cur` is a valid directory name, add to stack
                    stack.append(cur)
                # Reset `cur` for the next potential directory/file name
                cur = ""
            else:
                cur += ch  # Accumulate characters for the current directory/file name

        # Join the elements in the stack to form the simplified path
        return "/" + "/".join(stack)
