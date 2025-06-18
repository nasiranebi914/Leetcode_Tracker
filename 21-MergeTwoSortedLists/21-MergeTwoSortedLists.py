# Last updated: 6/17/2025, 10:35:20 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        l = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                l.next = list1
                list1 = list1.next
            else:
                l.next = list2
                list2 = list2.next
            l = l.next
        if list1:
            l.next = list1
        if list2:
            l.next = list2
        return dummy.next
            

        