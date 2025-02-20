class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the list to allow the use of the two-pointer technique
        nums.sort()
        nearby_target = float('inf')
        
        for i in range(len(nums)):
            # Initialize two pointers
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if abs(current_sum - target) < abs(nearby_target - target):
                    nearby_target = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target
        
        return nearby_target
