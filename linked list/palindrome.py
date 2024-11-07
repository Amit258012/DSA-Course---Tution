# https://leetcode.com/problems/palindrome-linked-list/

"""
To check if a linked list is a palindrome, we can use the "fast and slow pointer" technique to find the middle of the list. We then reverse the second half of the list and compare it with the first half. If all nodes match, the list is a palindrome. This approach allows us to check for palindrome properties with only one reversal of the second half and a single pass for comparison.

Time Complexity: O(n)
Space Complexity: O(1)
"""

"""
Try to solve brute force by storing values in arrays and comparing them. This solution has a time complexity of O(n) and a space complexity of O(n).
"""


from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev = None  # Initialize previous pointer as None for reversal
        cur = head  # Start with the head of the list
        nextNode = None  # Temporary pointer for the next node

        while cur:  # Traverse and reverse the list
            nextNode = cur.next  # Save the next node
            cur.next = prev  # Reverse the link
            prev = cur  # Move prev up to current node
            cur = nextNode  # Move cur to the saved next node
        return prev  # Return new head of reversed list

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head  # Initialize fast and slow pointers

        # Find the middle of the list
        while fast and fast.next:
            fast = fast.next.next  # Move fast pointer two steps
            slow = slow.next  # Move slow pointer one step

        # Reverse the second half of the list
        fast = head  # Reset fast to the head for comparison
        slow = self.reverseList(slow)  # Reverse the second half starting from slow

        # Compare the first and the second halves
        while slow:
            if slow.val != fast.val:  # If values are not equal, it's not a palindrome
                return False
            fast = fast.next  # Move to the next node in first half
            slow = slow.next  # Move to the next node in reversed second half
        return True  # If all nodes matched, the list is a palindrome
