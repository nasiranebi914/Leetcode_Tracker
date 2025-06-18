# Last updated: 6/17/2025, 10:35:22 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        '''
        # get the total length of the list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # if to remove head
        if length == n:
            return head.next
        
        # remove kth element
        current = head
        counter = 0
        while current:
            if length - counter == n + 1:
                print(length, counter, current)
                current.next = current.next.next
            counter += 1
            current = current.next
        return head
        '''
        dummy = ListNode(-1, head)
        slow=fast=dummy

        # Have n gap between fast and slow
        for i in range(n+1):
            fast = fast.next
        # Now fast and slow has n gaps, move slow to one before nth
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next # remove nth 
        return dummy.next
        