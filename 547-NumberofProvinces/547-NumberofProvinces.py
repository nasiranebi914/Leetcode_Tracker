# Last updated: 10/22/2025, 11:37:25 AM
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # build edges from the array isConnected
        edges = []
        n = len(isConnected)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    edges.append((i,j))
        
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
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootY] > rank[rootX]:
                parent[rootX] = rootY
            else:
                parent[rootX] = rootY
                rank[rootX] += 1
            return True
        
        count = n
        for v,e in edges:
            if union(v,e):
                count -= 1
        return count

            

