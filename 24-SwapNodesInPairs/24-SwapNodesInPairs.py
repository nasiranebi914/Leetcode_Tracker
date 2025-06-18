# Last updated: 6/17/2025, 10:35:17 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        current = head

        counter = 0

        while current is not None:
            counter += 1
            if counter == 2:
                tmp = prev.next
                prev.next = current
                tmp.next = current.next
                current.next = tmp

                prev = tmp
                current = tmp.next
                counter = 0
            else:
                current = current.next
        return dummy.next