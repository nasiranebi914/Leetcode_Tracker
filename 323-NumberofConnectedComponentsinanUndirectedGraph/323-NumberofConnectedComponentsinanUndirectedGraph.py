# Last updated: 8/4/2025, 7:11:56 PM
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
            elif rank[rootY] < rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True
        
        counter = n
        for v,e in edges:
            if union(v,e):
                counter -= 1 # everytime union returns True, decrease the number of total components, this way at the end counter will be the number of groups
        return counter