class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            visited[city] = True
            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        
        n = len(isConnected)
        visited = [False] * n
        provinces = 0
        for city in range(n):
            if not visited[city]:
                dfs(city)
                provinces += 1
        
        return provinces

# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         n = len(isConnected)
#         parent = [i for i in range(n)] # initially all are own parents

#         def find(x):
#             if parent[x] != x:
#                 parent[x] = find(parent[x]) # finding origin of child # Path compression
#             return parent[x]
        
#         def union(x, y):
#             rootx = find(x)
#             rooty = find(y)
#             if rootx != rooty:
#                 parent[rooty] = rootx # Merging of child to its parent # Union Operation

#         for i in range(n):
#             for j in range(i+1, n): # Traverse only uper triangular due to matrix symmetry
#                 if isConnected[i][j] == 1:
#                     union(i, j)
        
#         # Count number of distinct roots
#         provinces = len(set(find(i) for i in range(n)))
#         return provinces