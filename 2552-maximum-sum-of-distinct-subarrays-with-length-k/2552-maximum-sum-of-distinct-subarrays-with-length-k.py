class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        max_sum = 0
        current_sum = 0
        window_set = set()

        for right in range(len(nums)):
            # Shrink the window if duplicates are found
            while nums[right] in window_set:
                window_set.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            
            # Add the element to the window
            window_set.add(nums[right])
            current_sum += nums[right]
            
            # Check if the window size is exactly k
            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
                
                # Shrink the window to prepare for the next step
                current_sum -= nums[left]
                window_set.remove(nums[left])
                left += 1
        
        return max_sum