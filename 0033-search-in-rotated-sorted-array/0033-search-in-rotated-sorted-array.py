from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(log n)
        # Space Complexity: O(log n)
        def binary_search(left, right):
            if left > right:
                return -1  # Base case: not found

            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    return binary_search(left, mid - 1)  # Search left
                else:
                    return binary_search(mid + 1, right)  # Search right
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    return binary_search(mid + 1, right)  # Search right
                else:
                    return binary_search(left, mid - 1)  # Search left

        return binary_search(0, len(nums) - 1)




# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1
        
#         while left <= right:
#             mid = (left + right) // 2

#             if nums[mid] == target:
#                 return mid

#             # Left half is sorted
#             if nums[left] <= nums[mid]:
#                 if nums[left] <= target < nums[mid]:
#                     right = mid - 1  # Target is in the left half
#                 else:
#                     left = mid + 1   # Target is in the right half
#             else:
#                 # Right half is sorted
#                 if nums[mid] < target <= nums[right]:
#                     left = mid + 1  # Target is in the right half
#                 else:
#                     right = mid - 1  # Target is in the left half

#         return -1

