class Solution:
    def minDistance(self, word1: str, word2: str) -> int:    
        m, n = len(word1), len(word2)
        # Create a DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
    
        # Initialize the table
        for i in range(1, m + 1):
            dp[i][0] = i  # word1 to empty word2 (all deletions)
        for j in range(1, n + 1):
            dp[0][j] = j  # empty word1 to word2 (all insertions)
    
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1,  # Replace
                                   dp[i][j - 1] + 1,    # Insert
                                   dp[i - 1][j] + 1)    # Delete
    
        # The result is the value at the bottom-right of the table
        return dp[m][n]


# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         # Initialize a memoization dictionary to store results of subproblems
#         memo = {}
        
#         def recursiveSolution(i, j):
#             # Base Case 1: If we have exhausted all characters in word1
#             if i == len(word1):
#                 # The remaining characters in word2 need to be inserted
#                 return len(word2) - j
            
#             # Base Case 2: If we have exhausted all characters in word2
#             if j == len(word2):
#                 # The remaining characters in word1 need to be deleted
#                 return len(word1) - i
            
#             # Check if the result for this subproblem is already computed
#             if (i, j) in memo:
#                 return memo[(i, j)]
            
#             # If the current characters in word1 and word2 are the same,
#             # move to the next characters in both strings
#             if word1[i] == word2[j]:
#                 return recursiveSolution(i + 1, j + 1)
            
#             # Compute the cost of each operation:
#             # 1. Insert a character (move forward in word2)
#             insert = 1 + recursiveSolution(i, j + 1)
            
#             # 2. Delete a character (move forward in word1)
#             delete = 1 + recursiveSolution(i + 1, j)
            
#             # 3. Replace a character (move forward in both words)
#             replace = 1 + recursiveSolution(i + 1, j + 1)
            
#             # Take the minimum of the three operations and store it in the memo dictionary
#             memo[(i, j)] = min(insert, delete, replace)
#             return memo[(i, j)]
        
#         # Start the recursion from the beginning of both words
#         return recursiveSolution(0, 0)