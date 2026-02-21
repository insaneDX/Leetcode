class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        used = [False]*len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path.copy())
                return
            for i in range(len(nums)):
                if i>0 and nums[i] == nums[i-1] and not used[i-1]: # second twin cannot be choosen if first twin is not choosen to avoid duplicate branch
                    continue
                if used[i]:
                    continue
                used[i] = True 
                path.append(nums[i])
                backtrack(path)
                path.pop()

                used[i] = False
        
        backtrack([])

        return result