from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """        
        Time Complexity: O(amount * len(coins))
        - The outer loop runs `len(coins)` times.
        - The inner loop runs `amount` times for each coin.
        - Thus, the total time complexity is O(amount * len(coins)).

        Space Complexity: O(amount)
        - The space complexity is determined by the DP array `dp` of size `amount + 1`.
        """
        # Create a DP array to store the number of ways to make each amount
        dp = [0] * (amount + 1)
        
        # There is 1 way to make the amount 0: by using no coins
        dp[0] = 1
        
        # Iterate over each coin
        for coin in coins:
            # Update the DP array for all amounts that can include this coin
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        
        return dp[amount]


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         """
#         Time Complexity: O(amount * len(coins))
#         - The outer loop runs `amount` times.
#         - The inner loop runs `len(coins)` times.
#         - Thus, the total time complexity is O(amount * len(coins)).

#         Space Complexity: O(amount * len(coins))
#         - The space complexity is determined by the 2D DP array `dp` of size `(amount + 1) * (len(coins) + 1)`.
#         """
#         # Initialize a 2D array 'dp' to store the number of ways to make change
#         # for each amount using the given coin denominations.
#         dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]

#         # Base case: There's only one way to make change for amount 0 (no coins used).
#         dp[0] = [1] * (len(coins) + 1)

#         # Dynamic programming loop:
#         for a in range(1, amount + 1):
#             for i in range(len(coins) - 1, -1, -1):
#                 # Update the number of ways to make change for 'a' using coin 'coins[i]'.
#                 dp[a][i] = dp[a][i + 1]
#                 if a - coins[i] >= 0:
#                     dp[a][i] += dp[a - coins[i]][i]

#         # The final answer is stored in dp[amount][0].
#         return dp[amount][0]




# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         """ 
#         Time Complexity: O(amount * len(coins))
#         - The time complexity is determined by the number of subproblems, each of which is solved in constant time.
#         - There are `amount * len(coins)` unique subproblems, so the time complexity is O(amount * len(coins)).

#         Space Complexity: O(amount * len(coins))
#         - The space complexity is determined by the memoization dictionary, which stores results for `amount * len(coins)` subproblems.
#         - Additionally, there is a recursive call stack of depth `len(coins)` in the worst case, but this does not increase the overall space complexity.
#         """
#         memo = {}
        
#         def recursiveSolution(index, target):
#             # Check if the result is already in the memo dictionary
#             if (index, target) in memo:
#                 return memo[(index, target)]
            
#             # Base Case 1: If target is zero, we've found a valid combination
#             if target == 0:
#                 return 1
            
#             # Base Case 2: If no coins are left or target is negative, no valid combination
#             if index >= len(coins) or target < 0:
#                 return 0

#             # Option 1: Take the current coin and stay on the same index (allow repeated use)
#             take = recursiveSolution(index, target - coins[index])
            
#             # Option 2: Do not take the current coin and move to the next coin
#             not_take = recursiveSolution(index + 1, target)

#             # Store the result in the memo dictionary before returning it
#             memo[(index, target)] = take + not_take
            
#             return memo[(index, target)]
        
#         # Start the recursion from the first coin and the full amount
#         return recursiveSolution(0, amount)