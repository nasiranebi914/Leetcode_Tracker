# Last updated: 10/22/2025, 5:35:50 PM
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. build graph
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append([v,w])

        # 2. heapify
        heap = [[0,k]]
        visited = {}
        while heap:
            time,node = heapq.heappop(heap)
            if node not in visited:
                visited[node] = time
                for v,w in graph[node]:
                    new_time = time+w
                    heapq.heappush(heap, [new_time, v])
        return -1 if len(visited) < n else max(visited.values())
