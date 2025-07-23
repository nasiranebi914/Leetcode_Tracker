# Last updated: 7/23/2025, 10:28:23 AM
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        graph = defaultdict(list)
        for v,e in edges:
            graph[v].append(e)
            graph[e].append(v)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                if node == parent:
                    continue
                dfs(neighbor, node)
                    #return False
            return True
        return dfs(0,-1) and len(visited) == n
