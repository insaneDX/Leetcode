class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Initialize a memoization dictionary to store results of subproblems
        memo = {}
        
        def recursiveSolution(i, j):
            # Base Case 1: If we have exhausted all characters in word1
            if i == len(word1):
                # The remaining characters in word2 need to be inserted
                return len(word2) - j
            
            # Base Case 2: If we have exhausted all characters in word2
            if j == len(word2):
                # The remaining characters in word1 need to be deleted
                return len(word1) - i
            
            # Check if the result for this subproblem is already computed
            if (i, j) in memo:
                return memo[(i, j)]
            
            # If the current characters in word1 and word2 are the same,
            # move to the next characters in both strings
            if word1[i] == word2[j]:
                return recursiveSolution(i + 1, j + 1)
            
            # Compute the cost of each operation:
            # 1. Insert a character (move forward in word2)
            insert = 1 + recursiveSolution(i, j + 1)
            
            # 2. Delete a character (move forward in word1)
            delete = 1 + recursiveSolution(i + 1, j)
            
            # 3. Replace a character (move forward in both words)
            replace = 1 + recursiveSolution(i + 1, j + 1)
            
            # Take the minimum of the three operations and store it in the memo dictionary
            memo[(i, j)] = min(insert, delete, replace)
            return memo[(i, j)]
        
        # Start the recursion from the beginning of both words
        return recursiveSolution(0, 0)


