class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_sum = nums[0]
        max_sum = curr_sum

        for right in range(1, len(nums)):

            if curr_sum < 0:
                curr_sum = nums[right] # resetting the window on negative
            else:
                curr_sum += nums[right] # expanding the window on positive to maximize sum

            max_sum = max(max_sum, curr_sum)

        return max_sum

# At each index:

# Should I:
# 1. Extend current subarray?
# 2. Start a new one?