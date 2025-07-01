# Last updated: 7/1/2025, 6:51:55 PM
class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        # always add to low first
        heapq.heappush(self.low, -num)
        # move the largest of low to hight
        heapq.heappush(self.high, -heapq.heappop(self.low))
        # balance the heaps
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        # if low has more than high, return low
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return (-self.low[0] + self.high[0]) / 2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()