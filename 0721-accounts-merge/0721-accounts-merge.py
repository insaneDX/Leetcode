class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x  # First time seeing it
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX  # Union

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}

        # Step 1: Union all emails in the same account
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                uf.union(first_email, email)
                email_to_name[email] = name

        # Step 2: Group emails by their root
        merged = defaultdict(list)
        for email in email_to_name:
            root = uf.find(email)
            merged[root].append(email)

        # Step 3: Format result
        result = []
        for root_email, emails in merged.items():
            result.append([email_to_name[root_email]] + sorted(emails))
        return result
