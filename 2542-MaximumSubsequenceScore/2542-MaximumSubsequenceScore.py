# Last updated: 11/14/2025, 11:14:41 AM
class Solution(object):
    ''' 
    Problem: given n1,n2 find the maximum score: sum(k n1) * min(k n2)
    Trick: The most important factor the the min n2 number, so we sort n2 descending
    '''
    def maxScore(self, nums1, nums2, k):
        pairs = list(zip(nums2, nums1))
        pairs.sort(reverse=True)

        heap = []
        max_score = 0
        curr_sum = 0
        for n2,n1 in pairs:
            heapq.heappush(heap, n1)
            curr_sum += n1
            if len(heap) > k:
                curr_sum -= heapq.heappop(heap)
            if len(heap) == k:
                max_score = max(max_score, curr_sum*n2)
        return max_score
        
        