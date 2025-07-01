# Last updated: 7/1/2025, 4:03:28 PM
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in points:
            x = i[0]
            y = i[1]
            distance = x**2 + y**2
            heapq.heappush(heap, (-distance, [x,y]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [point for distance,point in heap]
        