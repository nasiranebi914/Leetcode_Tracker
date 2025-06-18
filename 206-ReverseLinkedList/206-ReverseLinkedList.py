# Last updated: 6/17/2025, 10:34:51 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head
        
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev
        