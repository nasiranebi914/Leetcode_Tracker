# Last updated: 7/10/2025, 10:21:01 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        dummy = ListNode(-1)
        current = dummy
        for node in lists:
            while node:
                heapq.heappush(heap,node.val)
                node = node.next
        while heap:
            current.next = ListNode(heapq.heappop(heap))
            current = current.next
        return dummy.next
            