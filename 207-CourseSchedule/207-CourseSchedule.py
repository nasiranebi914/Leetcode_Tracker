# Last updated: 10/22/2025, 11:50:10 AM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. build graph
        courses = defaultdict(list)
        degree = [0] * numCourses
        for v,e in prerequisites:
            courses[e].append(v)
            degree[v] += 1
        # 2. add 0 degree courses to the queue
        queue = deque([i for i in range(numCourses) if degree[i] == 0])

        # 3. start counting
        counter = 0
        while queue:
            course = queue.popleft()
            counter += 1
            for neighbor in courses[course]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
        return counter == numCourses
        




        
        
        