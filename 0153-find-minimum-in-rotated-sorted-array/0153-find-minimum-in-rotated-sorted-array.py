from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Time Complexity: O(log n)
        #Space Complexity: O(log n)
        def binary_search(left, right):
            # Base case: if the search window is down to 1 element
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2

            # If mid element is greater than right, min is in right half
            if nums[mid] > nums[right]:
                return binary_search(mid + 1, right)
            else:
                # Otherwise, min is in the left half (including mid)
                return binary_search(left, mid)

        return binary_search(0, len(nums) - 1)



# class Solution:
#     def findMin(self, nums: List[int]) -> int:
          #Time Complexity: O(log n)
          #Space Complexity: O(1)
#         left, right = 0, len(nums) - 1

#         while left < right:
#             mid = (left + right) // 2

#             # If mid element is greater than right, minimum must be on the right
#             if nums[mid] > nums[right]:
#                 left = mid + 1
#             else:
#                 # Minimum is at mid or to the left of mid
#                 right = mid

#         # At the end, left == right and points to the smallest value
#         return nums[left]

