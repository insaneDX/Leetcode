class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        # Initialize parent if x not seen before
        if x not in self.parent:
            self.parent[x] = x
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        # Merge if in different groups
        if root_x != root_y:
            self.parent[root_y] = root_x


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        uf = UnionFind()

        # Check if two strings are similar (differ in 0 or exactly 2 positions)
        def are_similar(s1, s2):
            diff = []
            for a, b in zip(s1, s2):
                if a != b:
                    diff.append((a, b))
            return len(diff) == 2 and diff[0] == diff[1][::-1] or len(diff) == 0

        # Union all similar strings
        n = len(strs)
        for i in range(n):
            for j in range(i + 1, n): 
                if are_similar(strs[i], strs[j]):
                    uf.union(strs[i], strs[j])

        # Count unique groups by root parents
        groups = set()
        for s in strs:
            groups.add(uf.find(s))

        return len(groups)
