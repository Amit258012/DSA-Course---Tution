# https://leetcode.com/problems/reverse-linked-list/description/

"""
To reverse a linked list, we iterate through each node while keeping track of the previous node. At each step, we reverse the direction of the current node’s next pointer to point to the previous node instead of the next. We then move forward in the list by updating our pointers, and by the end of the loop, prev will point to the new head of the reversed list.

Time Complexity: O(n)
Space Complexity: O(1)
"""


from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # Initialize previous node as None (new tail)
        cur = head  # Start with the head of the list
        nextElem = None  # Temporary pointer for the next node

        while cur:  # Traverse until we reach the end of the list
            nextElem = cur.next  # Save the next node
            cur.next = prev  # Reverse the link: make current node point to previous
            prev = cur  # Move prev up to current node
            cur = nextElem  # Move cur to the saved next node

        return prev  # At the end, prev will be the new head of the reversed list
