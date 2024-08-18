class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Initialize parent pointers for each node
        self.rank = [1] * n           # Rank to track depth/max_height of a node
        self.size = [1] * n           # To track size of a node
        self.edge_count = [0] * n     # To track edges from a node 

    def find_parent(self, node):      # Function to find root ancestor
        curr = node
        while curr != self.parent[curr]:  # Path compression
            self.parent[curr] = self.parent[self.parent[curr]] 
            curr = self.parent[curr]
        return curr

    def union(self, u, v):            # Union operation
        p1, p2 = self.find_parent(u), self.find_parent(v)

        # Merge small component into larger component, increment size and edge count + 1 (extra edge while merging)
        if p1 != p2:                  # If ancestors are not the same, merge else add 1 edge
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
                self.size[p1] += self.size[p2]
                self.edge_count[p1] += self.edge_count[p2] + 1

            elif self.rank[p1] < self.rank[p2]:
                self.parent[p1] = p2
                self.size[p2] += self.size[p1]
                self.edge_count[p2] += self.edge_count[p1] + 1

            else:                     # If both ranks are the same, merge and increment rank as rank is max_height of tree
                self.rank[p1] += 1
                self.parent[p2] = p1
                self.size[p1] += self.size[p2]
                self.edge_count[p1] += self.edge_count[p2] + 1
        else:
            self.edge_count[p1] += 1  # If already in the same component, just add an edge


class Solution:
    def countCompleteComponents(self, n, edges):
        uf = UnionFind(n)
        for u, v in edges:
            # Perform union find operations
            uf.union(u, v)
        
        components_edges = {}  # To track parent edges
        for node in range(n):
            curr = uf.find_parent(node)
            if curr not in components_edges:
                components_edges[curr] = 0
            components_edges[curr] = uf.edge_count[curr]

        complete_components = 0
        for node in components_edges:
            edges = uf.edge_count[node]
            size = uf.size[node]
            if edges == size * (size - 1) // 2:  # Formula --> edge = size * (size-1)//2
                complete_components += 1
        
        return complete_components


