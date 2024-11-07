# https://leetcode.com/problems/linked-list-cycle/

"""
We initialize two pointers, slow and fast, both starting at the head. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If there is a cycle, the fast pointer will eventually meet the slow pointer inside the cycle. If the fast pointer reaches the end of the list (None), we can be sure that there is no cycle.

Time Complexity: O(n)
Space Complexity: O(1)
"""


from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head  # Initialize fast pointer at the head
        slow = head  # Initialize slow pointer at the head
        while fast and fast.next:  # Continue until fast reaches the end
            fast = fast.next.next  # Move fast two steps
            slow = slow.next  # Move slow one step
            if fast == slow:  # If fast meets slow, there's a cycle
                return True
        return False  # If fast reaches the end, there's no cycle
