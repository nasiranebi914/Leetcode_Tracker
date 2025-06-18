# Last updated: 6/17/2025, 10:35:08 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=current=head

        while current:
            if prev.val == current.val:
                tmp = current.next
                prev.next = tmp
                current = tmp
            else:
                current = current.next
                prev = prev.next
        return head
        