# https://leetcode.com/problems/rotate-list/

"""
To rotate a linked list to the right by 
k places, we observe that rotating a list by its length (or any multiple of it) leaves the list unchanged. Thus, we first calculate the length of the list and adjust k by taking mod length k mod length. We then use two pointers (fast and slow) to find the new head. The fast pointer is movedk nodes ahead of slow, and both pointers then move until fast reaches the end. The slow.next node will then be the new head of the rotated list, and we rearrange the pointers accordingly.


Time Complexity: O(n)
Space Complexity: O(1)
"""


from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:  # If list is empty, return None
            return head

        # Step 1: Calculate the length of the list
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        # Step 2: Adjust k to be within the length of the list
        k = k % length
        if k == 0:  # No rotation needed if k is 0 after modulo operation
            return head

        # Step 3: Set up two pointers, fast and slow, with fast k nodes ahead of slow
        fast = head
        slow = head
        for _ in range(k):
            fast = fast.next

        # Step 4: Move both pointers until fast reaches the last node
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Step 5: Set the new head and rearrange pointers to rotate the list
        newHead = slow.next  # New head is the next node after slow
        slow.next = None  # Break the list at slow
        fast.next = head  # Connect the end of the list to the original head

        return newHead  # Return the new head of the rotated list
