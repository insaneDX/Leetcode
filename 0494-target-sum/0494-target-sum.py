class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(n*target)
        # Space Complexity: O(n*target)

        n = len(nums)
        memo = {}
        
        def recursive(n, count):
            if n == 0:
                return 1 if count == target else 0
            if (n, count) in memo:
                return memo[(n, count)]
            add = recursive(n-1, count + nums[n-1])
            sub = recursive(n-1, count - nums[n-1])
            memo[(n, count)] = add + sub
            return memo[(n, count)]
        
        return recursive(n,0)