class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        used = [False]*len(nums) # space O(n)

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False
        backtrack([])

        return result

# Time complexity: n! permutations × O(n) = O(n⋅n!)

# Space complexigy: Recursion Stack Maximum depth = n; O(n)
# output storage: O(n⋅n!)
# Final O(n⋅n!) (output storage + used array + recursion stack)
# Auxiliary space only (excluding output):𝑂(𝑛)O(n)