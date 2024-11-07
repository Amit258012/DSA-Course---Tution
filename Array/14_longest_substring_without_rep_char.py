# https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
We use the sliding window technique with two pointers: left_pointer and right_pointer to maintain a window of unique characters.
A set (char_set) is used to keep track of the characters in the current window.
If a character at right_pointer is already in the set, we move the left_pointer to the right until we remove the duplicate character from the set.
At each step, we calculate the current window size (right_pointer - left_pointer + 1) and update the maximum length of the substring without repeating characters.

Time Complexity: O(n)
Space Complexity: O(1)
"""

"""
Can you solve it by different way ? Anyway try to do it😅
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # A set to store the unique characters of the current window
        n = len(s)  # Length of the input string
        left_pointer = 0  # Left pointer for the sliding window
        max_length = 0  # To store the result (length of the longest substring)

        # Traverse through the string using a right pointer
        for right_pointer in range(n):
            # If the character at the right pointer is already in the set,
            # shrink the window from the left until the duplicate is removed
            while s[right_pointer] in char_set:
                char_set.remove(s[left_pointer])  # Remove the character from the set
                left_pointer += 1  # Move the left pointer to the right

            # Add the current character to the set
            char_set.add(s[right_pointer])

            # Update the result with the current window size
            max_length = max(max_length, right_pointer - left_pointer + 1)

        return max_length
