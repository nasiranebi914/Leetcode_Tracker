# Last updated: 10/22/2025, 11:36:03 AM
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # build edges that has the connected nodes
        edges = []
        n = len(isConnected)
        for i in range(n):
            for j in range(i+1, n): # to avoid duplicates and self loop
                if isConnected[i][j] == 1:
                    edges.append((i,j))
        # union find
        parent = list(range(n))
        rank = [1] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootY] < rank[rootX]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True
        
        counter = n
        for v,e in edges:
            if union(v,e):
                counter -= 1
        return counter
