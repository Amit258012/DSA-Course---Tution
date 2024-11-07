# https://leetcode.com/problems/middle-of-the-linked-list/description/

"""
We initialize two pointers, slow and fast, both starting at the head. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. By the time fast reaches the end of the list, slow will be at the middle. This approach ensures that we only traverse the list once.

Time Complexity: O(n)
Space Complexity: O(1)
"""


from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head  # Initialize both pointers at the head
        while fast and fast.next:  # Continue until fast reaches the end
            slow = slow.next  # Move slow one step
            fast = fast.next.next  # Move fast two steps
        return slow  # When fast reaches the end, slow will be at the middle
