class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity:
        # Total time = O(log n)
        # Total space = O(log n)
        left, right = 0, len(nums) - 1

        # Recursive binary search to find the first (leftmost) index of the target
        def search_first(left, right):
            if left > right:
                return -1  # Base case: target not found in current search space

            mid = (left + right) // 2

            if nums[mid] == target:
                # If mid is the first element, or the element before mid is not target,
                # then mid is the first occurrence
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                else:
                    # Keep searching in the left half to find an earlier occurrence
                    return search_first(left, mid - 1)
            elif nums[mid] < target:
                # Target must be in the right half
                return search_first(mid + 1, right)
            else:
                # Target must be in the left half
                return search_first(left, mid - 1)

        # Recursive binary search to find the last (rightmost) index of the target
        def search_last(left, right):
            if left > right:
                return -1  # Base case: target not found in current search space

            mid = (left + right) // 2

            if nums[mid] == target:
                # If mid is the last element, or the element after mid is not target,
                # then mid is the last occurrence
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                else:
                    # Keep searching in the right half to find a later occurrence
                    return search_last(mid + 1, right)
            elif nums[mid] < target:
                # Target must be in the right half
                return search_last(mid + 1, right)
            else:
                # Target must be in the left half
                return search_last(left, mid - 1)

        # Run both recursive functions to find first and last indices
        start = search_first(left, right)
        end = search_last(left, right)

        return [start, end]



# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         # Time Complexity:
#         # Total time = O(log n)
#         # Total space = O(1)
#         def find_first(nums, target):
#             left, right = 0, len(nums) - 1
#             index = -1
#             while left <= right:
#                 mid = (left + right) // 2
#                 if nums[mid] == target:
#                     index = mid
#                     right = mid - 1  # keep searching to the left
#                 elif nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             return index

#         def find_last(nums, target):
#             left, right = 0, len(nums) - 1
#             index = -1
#             while left <= right:
#                 mid = (left + right) // 2
#                 if nums[mid] == target:
#                     index = mid
#                     left = mid + 1  # keep searching to the right
#                 elif nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             return index

#         start = find_first(nums, target)
#         end = find_last(nums, target)
#         return [start, end]
