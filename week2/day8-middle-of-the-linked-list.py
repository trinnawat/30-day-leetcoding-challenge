'''
    https://leetcode.com/problems/middle-of-the-linked-list
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head.next is None:
            return head
        if head.next.next is None:
            return head.next
        next_head = head.next
        next_next_head = head.next.next
        while True:
            if next_next_head is None:
                break
            if next_next_head.next is None:
                break
            next_head = next_head.next
            next_next_head = next_next_head.next.next
        return next_head
