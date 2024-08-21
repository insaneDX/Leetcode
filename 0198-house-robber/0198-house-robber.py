class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(mums, n, memo):
            if n < 0:
                return 0
            if memo[n] != -1:
                return memo[n]
            rob = nums[n] + helper(nums, n-2, memo)
            skip = helper(nums, n-1, memo)
            memo[n] = max(rob, skip)
            return memo[n]

        n = len(nums)
        memo = [-1 for i in range(n)]
        return max (helper(nums, n-1, memo), helper(nums, n-2, memo))