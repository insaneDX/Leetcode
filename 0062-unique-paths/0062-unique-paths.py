class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the bottom-right corner since there's only one way to reach there
        dp[m - 1][n - 1] = 1
        
        # Fill the DP table from bottom-right to top-left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    dp[i][j] += dp[i + 1][j]  # move down from the cell below
                if j < n - 1:
                    dp[i][j] += dp[i][j + 1]  # move right from the cell
        
        # The top-left corner will have the number of unique paths
        return dp[0][0]

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         memo: Dict[Tuple[int, int], int] = {}
        
#         def dfs(i: int, j: int) -> int:
#             if i == m - 1 and j == n - 1:  # reached the bottom-right corner
#                 return 1
#             if i >= m or j >= n:  # out of bounds
#                 return 0
            
#             if (i, j) in memo:  # return cached result if available
#                 return memo[(i, j)]
            
#             right = dfs(i, j + 1)  # move right
#             down = dfs(i + 1, j)   # move down
            
#             memo[(i, j)] = right + down  # store result in memoization table
#             return memo[(i, j)]
        
#         return dfs(0, 0)