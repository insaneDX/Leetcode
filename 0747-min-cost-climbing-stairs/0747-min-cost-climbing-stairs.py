""" step_1 is the cost of taking one step from the n-th stair plus the minimum cost to get to the n-1-th stair.
    step_2 is the cost of taking two steps from the n-1-th stair plus the minimum cost to get to the n-2-th stair.
    dp[n] is the minimum of these two values, which is stored in the memoization array."""

class Solution:
    def helper(self, cost, n, dp):
        # Base case: no cost when beyond the first step
        if n < 0:
            return 0
        # If the cost for this step has already been computed, return it
        if dp[n] != -1:
            return dp[n]
        # Compute the cost if we decide to step from n-1 or n-2
        step_1 = cost[n] + self.helper(cost, n - 1, dp)
        step_2 = cost[n] + self.helper(cost, n - 2, dp)
        # Store the minimum of these two choices
        dp[n] = min(step_1, step_2)
        return dp[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1 for _ in range(n)]
        # You can end up either at the last or second last step, so compare both
        return min(self.helper(cost, n - 1, dp), self.helper(cost, n - 2, dp))

# Example usage
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
solution = Solution()
print(solution.minCostClimbingStairs(cost))  # Expected output: 6

