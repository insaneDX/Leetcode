class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initialize the sum of the first window
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Slide the window across the array
        for i in range(k, len(nums)):
            # Subtract the element leaving the window and add the new one
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        # Return the maximum average
        return max_sum / k

# Time: O(n)
# Space: O(1)