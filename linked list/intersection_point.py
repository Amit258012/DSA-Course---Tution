# https://leetcode.com/problems/intersection-of-two-linked-lists/

"""
To find the intersection node of two singly linked lists, we use two pointers, p1 and p2, starting at the heads of headA and headB. We advance each pointer by one step through their respective lists. When a pointer reaches the end of its list, we reset it to the head of the other list. This way, both pointers will traverse both lists once and meet at the intersection node if one exists, or reach None at the same time if there is no intersection.

Time Complexity: O(n + m)
Space Complexity: O(1)
"""

"""
Try to solve brute force using set() to store the nodes of one list and then traverse the other list to check if the node is in the set. This solution has a time complexity of O(n + m) and a space complexity of O(n) or O(m) depending on the size of the set.
"""


from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:

        p1 = headA  # Pointer for list A
        p2 = headB  # Pointer for list B

        while p1 != p2:
            # If p1 reaches the end of list A, switch to head of list B
            p1 = p1.next if p1 else headB
            # If p2 reaches the end of list B, switch to head of list A
            p2 = p2.next if p2 else headA

        # Either returns the intersection node or None if there is no intersection
        return p1
