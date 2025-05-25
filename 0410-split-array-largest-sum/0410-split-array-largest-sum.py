from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def can_split(max_allowed_sum):
            current_sum = 0
            subarray = 1

            for num in nums:
                if current_sum + num > max_allowed_sum:
                    subarray += 1
                    current_sum = 0
                current_sum += num

            return subarray <= k

        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1

        return left

# Time Complexity: O(n⋅log(sum(nums)−max(nums)))
# Space Complexity: O(1)
