# Last updated: 7/23/2025, 3:15:18 PM
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create graph and count the degrees
        graph = defaultdict(list)
        degree = [0] * numCourses
        for v,e in prerequisites:
            graph[e].append(v)
            degree[v] += 1
        # create queue for the 0 degree
        queue = deque([i for i in range(numCourses) if degree[i] == 0])
        # bfs
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result if numCourses == len(result) else []
        