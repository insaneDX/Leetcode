class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        result = []
        def backtrack(start,path):
            if len(path) == k:
                result.append(path.copy())
                return
            
            for i in range(start, len(nums)):
                
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])

        return result