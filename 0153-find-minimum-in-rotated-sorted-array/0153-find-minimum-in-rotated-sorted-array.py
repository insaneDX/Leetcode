from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        # If the array is not rotated, the minimum is the first element
        if nums[left] < nums[right]:
            return nums[left]

        while left < right:
            mid = (left + right) // 2

            # Check if mid is the minimum
            if nums[mid] < nums[mid - 1]: #[7,5,3,0,1,2] If the right element of the left partition is greater than the middle element, this is the breaking point.
                return nums[mid]
            elif nums[mid] > nums[right]:
                # Minimum is in the right part
                left = mid + 1
            else:
                # Minimum is in the left part
                right = mid - 1

        return nums[left]
