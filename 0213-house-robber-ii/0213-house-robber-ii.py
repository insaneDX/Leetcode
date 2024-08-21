class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums, n, memo):

            # Base case: If no houses are left to rob, return 0
            if n < 0:
                return 0
            
            # If the result for this house is already computed, return it
            if memo[n] != -1:
                return memo[n]
            
            # Calculate the maximum money by either robbing this house or not robbing it
            rob_current = nums[n] + helper(nums, n - 2, memo)  # Rob this house and skip the next one
            skip_current = helper(nums, n - 1, memo)  # Skip this house and check the next one
            
            # Store the maximum of the two choices in memo and return it
            memo[n] = max(rob_current, skip_current)
            return memo[n]

        n = len(nums)
        # Edge case: if there are no houses to rob
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        # Initialize memoization array with -1
        memo1 = [-1 for _ in range(n-1)]
        memo2 = [-1 for _ in range(n-1)]

        
        # The result will be the maximum of either robbing the last house or skipping it
        return max(helper(nums[1:], n - 2, memo1), helper(nums, n - 2, memo2))