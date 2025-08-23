class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1}
        curr_sum, count = 0,0

        # Track prefix sums and their frequencies to count subarrays summing to k.
        # Initialize with {0:1} to handle subarrays starting at index 0.

        for num in nums:
            curr_sum += num
            count += prefix_sum.get(curr_sum-k,0)
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
        
        return count

#Time Complexity: O(n) — where n is the number of elements in nums.
#Space Complexity: O(n) — in the worst case, the prefix_sum dictionary could store up to n unique prefix sums.


        