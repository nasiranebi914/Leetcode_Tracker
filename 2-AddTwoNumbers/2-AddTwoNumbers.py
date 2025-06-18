# Last updated: 6/17/2025, 10:35:53 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        tmp = 0
        dummy = ListNode(-1)
        l = dummy

        while l1 or l2 or tmp:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + tmp
            digit = total % 10
            tmp = total // 10

            l.next = ListNode(digit)
            l = l.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

            