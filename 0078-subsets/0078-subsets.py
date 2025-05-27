class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []

        def dfs(i, path):
            if i >= len(nums):  # Base case: when index exceeds list length
                subset.append(path.copy())  # Store a valid subset
                return

            # Include nums[i] in the subset
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()  # Backtrack

            # Exclude nums[i] and move forward
            dfs(i + 1, path)

        dfs(0, [])  # Start DFS traversal
        return subset