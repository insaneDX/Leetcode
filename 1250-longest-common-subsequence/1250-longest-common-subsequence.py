class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = {}  # Memoization dictionary to store computed results

        def reconstruct_lcs(m, n):
            # Function to reconstruct the Longest Common Subsequence
            lcs = []
            while m > 0 and n > 0:
                if text1[m-1] == text2[n-1]:
                    # If characters match, add to LCS and move diagonally
                    lcs.append(text1[m-1])
                    m -= 1
                    n -= 1
                elif memo.get((m-1, n), 0) > memo.get((m, n-1), 0):
                    # If up value is greater, move up
                    m -= 1
                else:
                    # Otherwise, move left
                    n -= 1
            return ''.join(reversed(lcs))  # Reverse LCS before returning

        def lcs(m, n):
            # Recursive function to compute LCS length with memoization
            if m == 0 or n == 0:
                # Base case: if either string is empty, LCS length is 0
                return 0
            if (m, n) in memo:
                # If result is memoized, return it
                return memo[(m, n)]
            if text1[m-1] == text2[n-1]:
                # If characters match, include it in LCS and recurse
                result = 1 + lcs(m-1, n-1)
            else:
                # If characters don't match, take max of two possibilities
                result = max(lcs(m-1, n), lcs(m, n-1))
            
            memo[(m, n)] = result
            return result

        return lcs(m, n)
