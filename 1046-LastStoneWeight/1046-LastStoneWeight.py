# Last updated: 7/1/2025, 2:45:33 PM
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)
        
        while len(heap) > 1:
            x = heapq.heappop(heap) * -1
            y = heapq.heappop(heap) * -1
            if x != y:
                heapq.heappush(heap,abs(y-x)*-1)
        if heap: return -1 * heap[0]
        return 0
        