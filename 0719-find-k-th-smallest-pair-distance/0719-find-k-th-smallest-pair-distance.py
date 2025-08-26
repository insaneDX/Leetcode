class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        # Binary search over the possible pair distances
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            count = self.count_pairs_with_max_distance(nums, mid)

            # If there are fewer than k pairs with distance ≤ mid, we need a larger distance
            if count < k:
                left = mid + 1
            else:
                right = mid  # mid might be the answer, so we keep it

        return left  # left is the smallest distance with at least k pairs

    def count_pairs_with_max_distance(self, nums: List[int], max_distance: int) -> int:
        count = 0
        left = 0

        # Use sliding window to count valid pairs with distance ≤ max_distance
        for right in range(len(nums)):
            while nums[right] - nums[left] > max_distance:
                left += 1
            count += right - left  # all pairs (left, left+1, ..., right-1) are valid

        return count


# Time Complexity:O(n log n) - The dominant operations are sorting the array, which takes O(n log n) time, and the binary search, which has a time complexity of O(log(max_distance)) * O(n), where O(n) is the time taken by the sliding window to count pairs. The sorting step dominates, making the total time complexity O(n log n).

# Space Complexity: O(1)