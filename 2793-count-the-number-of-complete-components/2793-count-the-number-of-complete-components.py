class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n
        self.edge_count = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
                self.edge_count[rootX] += self.edge_count[rootY] + 1
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
                self.edge_count[rootY] += self.edge_count[rootX] + 1
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
                self.size[rootX] += self.size[rootY]
                self.edge_count[rootX] += self.edge_count[rootY] + 1
        else:
            self.edge_count[rootX] += 1

class Solution:
    def countCompleteComponents(self, n, edges):
        uf = UnionFind(n)
        
        # Perform union operations for all edges
        for u, v in edges:
            uf.union(u, v)

        # Count the complete components
        component_edges = {}
        for i in range(n):
            root = uf.find(i)
            if root not in component_edges:
                component_edges[root] = 0
            component_edges[root] = uf.edge_count[root]
        
        complete_components = 0
        for root in component_edges:
            size = uf.size[root]
            edges = uf.edge_count[root]
            if edges == size * (size - 1) // 2:
                complete_components += 1
        
        return complete_components


