# Last updated: 10/22/2025, 6:59:03 PM
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s,d,p in flights:
            graph[s].append([d,p])

        heap = [[0,src,0]]
        visited = {}
        prices = []
        while heap:
            price,node,stops = heapq.heappop(heap)
            if node == dst and stops <= k+1:
                return price
            if stops > k:
                continue
            if (node in visited and visited[node] <= stops):
                continue
            visited[node] = stops

            for d,p in graph[node]:
                heapq.heappush(heap, [p+price, d, stops+1])
        return -1