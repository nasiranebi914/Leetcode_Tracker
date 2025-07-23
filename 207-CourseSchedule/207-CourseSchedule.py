# Last updated: 7/23/2025, 2:39:30 PM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a graph and count the degrees
        graph = defaultdict(list)
        degree = [0] * numCourses
        for v,e in prerequisites:
            graph[e].append(v)
            degree[v] += 1
        # create a queue with the 0 degrees
        queue = deque([i for i in range(numCourses) if degree[i] == 0])
        
        # start bfs
        counter = 0
        while queue:
            node = queue.popleft()
            counter += 1
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
        return counter == numCourses
        
        