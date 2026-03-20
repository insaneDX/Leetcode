# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         memo = {}
#         def dfs(n):
#             if n >= len(nums)-1:
#                 return True
            
#             if n in memo:
#                 return memo[n]
            
#             for jump in range(1, nums[n]+1):
#                 if dfs(n + jump):
#                     memo[n] = True
#                     return True
            
#             memo[n] = False
#             return False

            
#             return False
#         return dfs(0)

class Solution:
    def canJump(self, nums):
        goal = len(nums)-1
    
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
            
        return True if goal == 0 else False