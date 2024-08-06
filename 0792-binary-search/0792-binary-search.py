class Solution:
    def helper(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1  # Target not found

        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            # Search right portion
            return self.helper(nums, target, mid + 1, right)

        else:
            # Search left portion
            return self.helper(nums, target, left, mid - 1)

    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0, len(nums) - 1)
