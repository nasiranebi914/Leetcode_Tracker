# Last updated: 8/22/2025, 5:30:06 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find middle
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        # reverse second half
        prev = None
        curr = slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # compare the two halves
        curr = head
        p = prev
        while p:
            if curr.val != p.val:
                return False
            curr = curr.next
            p = p.next
        return True