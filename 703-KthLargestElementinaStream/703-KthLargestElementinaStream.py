# Last updated: 6/27/2025, 11:09:45 PM
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for i in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, i)
            elif i > self.heap[0]:
                heapq.heappushpop(self.heap, i)
        
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)