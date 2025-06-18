# Last updated: 6/17/2025, 10:35:03 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow=fast=head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None # this else is executed if the while loop didn't break
        slow=head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
        