# Last updated: 8/4/2025, 5:50:15 PM
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree is valid if there is no cycle, and all nodes are connected
        # to detect if all nodes are connected, we use below
        if len(edges) != n-1:
            return False
        # We can use union find to detect cycle

        # 1. initilize parents and rank
        parents = list(range(n))
        rank = [1] * n
        # 2. find function, compress the tree
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        # 3. union
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False # cycle detected!
            if rank[rootX] < rank[rootY]:
                parents[rootX] = rootY
            elif rank[rootY] < rank[rootX]:
                parents[rootY] = rootX
            else:
                parents[rootY] = rootX
                rank[rootX] += 1
            return True
        # 4. call the functions
        for v,e in edges:
            if not union(v,e):
                return False
        return True
        