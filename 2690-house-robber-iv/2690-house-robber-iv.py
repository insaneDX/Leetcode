class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        def can_rob_with_capability(cap):
            count = 0
            i = 0
            while i<len(nums):
                if nums[i] <= cap:
                    count += 1 # Rob this house
                    i += 1 # Skip the next house (no adjacent robbery)
                i += 1
            
            return count >= k # if can be robbed >= k houses
        
        left = min(nums)
        right = max(nums)
        while left < right:
            mid = (left + right)//2
            if can_rob_with_capability(mid):
                right = mid # Try a smaller capability
            else: 
                left = mid+1 # Increase capability
        
        return left # Smallest capability that allows robbing at least k houses
        

        