class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize the first two steps
        prev_1 = 1  # This represents the number of ways to reach the (i-1)th step
        prev_2 = 1  # This represents the number of ways to reach the (i-2)th step

        # Iterate from the 2nd step to the nth step
        for i in range(2, n + 1):
            # Calculate the number of ways to reach the current step
            sum = prev_1 + prev_2
            # Update prev_2 to be the previous step's value
            prev_2 = prev_1
            # Update prev_1 to be the current step's value
            prev_1 = sum
        
        # Return the number of ways to reach the nth step
        return prev_1


# # memoized version
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         memo = [-1] * (n + 1)
#         return self._climbStairs(n, memo)
    
#     def _climbStairs(self, n: int, memo: List[int]) -> int:
#         if n <= 1:
#             return 1
#         if memo[n] != -1:
#             return memo[n]
#         memo[n] = self._climbStairs(n - 1, memo) + self._climbStairs(n - 2, memo)
#         return memo[n]



# # recursive version
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         Base case: If there are 0 or 1 steps, there's only one way to climb them
#         if n <= 1:
#             return 1

#         # Recursive calls
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)
