class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []
        def backtrack(start, path):
            result.append(path.copy())
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()


        backtrack(0, [])

        return result

# time complexity: O(n.2^n)
# space complexity:  O(n⋅2^n) (including output and auxilary space)
# recursion stack : O(n) and output stack  O(n⋅2^n)