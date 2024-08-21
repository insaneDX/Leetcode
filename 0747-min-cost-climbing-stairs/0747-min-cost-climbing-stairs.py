class Solution:
    def helper(self, cost, n, dp):
        if n < 1:
            return 0
        if dp[n] != -1:
            return dp[n]
        step_1 = cost[n] + self.helper(cost, n-1, dp)
        step_2 = cost[n-1] + self.helper(cost, n-2, dp)
        dp[n] = min(step_1, step_2)
        return dp[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)-1
        dp = [-1 for i in range(n+1)]
        return self.helper(cost, n, dp)
        