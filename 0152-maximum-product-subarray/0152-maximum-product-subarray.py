class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) <= 1:
            return nums[0]
            
        curr_min = nums[0]
        curr_max = nums[0]

        maximum = nums[0]

        for num in nums[1:]:

            if num < 0:
                curr_min, curr_max = curr_max, curr_min
            
            curr_max = max(num, curr_max*num)
            curr_min = min(num, curr_min*num)

            maximum = max(maximum, curr_max)

        return maximum