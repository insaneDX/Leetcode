class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for i in range (amount + 1)]
        dp[0] = 0

        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
        
#         def helper(coins, amount, n, memo):
#             # Base case: if the amount is 0, no coins are needed
#             if amount == 0:
#                 return 0
            
#             # If no coins are left or the amount is negative, return infinity (impossible case)
#             if n < 0 or amount < 0:
#                 return float('inf')
            
#             # If the result is already computed, return it from memo
#             if memo[n][amount] != -1:
#                 return memo[n][amount]

#             # Include the current coin and make a recursive call with reduced amount
#             include = 1 + helper(coins, amount - coins[n], n, memo)
#             # Exclude the current coin and make a recursive call with the next coin
#             exclude = helper(coins, amount, n - 1, memo)
#             # Store the result in memo and return the minimum of including or excluding the coin
#             memo[n][amount] = min(include, exclude)

#             return memo[n][amount]

#         n = len(coins)
#         memo = [[-1 for _ in range(amount + 1)] for _ in range(n)]
#         result = helper(coins, amount, n - 1, memo)
#         # If the result is infinity, return -1 (not possible to make the amount), otherwise return the result
#         return -1 if result == float('inf') else result

