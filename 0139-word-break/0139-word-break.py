class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict) # cutting time complexity to o(1) search
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True 

        # Input: s = "leetcode", wordDict = ["leet","code"]
        # Output: true
        # [  l e e t c o d e]
        # [T F F F T F F F T]
        # at index ith check uptill i can we make a string? this scanning has overlap so it is overlaping problem.

        # constraints
        # 1 <= wordDict[i].length <= 20 and 1 <= s.length <= 300

        for i in range(1, n+1): # n times
            for j in range(i):  # n times
                if dp[j] and s[j: i] in wordSet: # substring creation s[j: i] o(n)
                    dp[i] = True
                    break
        
        return dp[n]

# Time complexity O(n^3)
# Space complexity O(n + m) # n for dp and m for wordSet creation