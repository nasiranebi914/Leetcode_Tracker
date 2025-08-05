# Last updated: 8/4/2025, 7:28:32 PM
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        rank = [1] * (n+1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False # detected cycle
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootY] < rank[rootX]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True
        
        for v,e in edges:
            if not union(v,e):
                return [v,e]
        