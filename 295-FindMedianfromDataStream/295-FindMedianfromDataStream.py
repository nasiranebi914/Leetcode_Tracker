# Last updated: 7/22/2025, 9:52:13 PM
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build graph from edges first
        graph = defaultdict(list)
        for v,e in edges:
            graph[v].append(e)
            graph[e].append(v) # edges are undirected 

        counter = 0
        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                counter += 1

        return counter