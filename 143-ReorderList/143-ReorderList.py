# Last updated: 6/17/2025, 10:35:02 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        # Find the middle
        slow=fast=head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        current = slow.next
        slow.next = None
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp

        # Merge two parts
        l1 = head
        l2 = prev
        ans = ListNode()
        while l2:
            tmp1 = l1.next
            tmp2 = l2.next
            l1.next = l2
            l2.next = tmp1           
            l1 = tmp1
            l2 = tmp2
        