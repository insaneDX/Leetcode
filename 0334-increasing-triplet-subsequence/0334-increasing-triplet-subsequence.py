class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n  # Update the smallest number
            elif n <= second:
                second = n  # Update the second smallest number
            else:
                # If we find a number greater than both first and second,
                # we have found an increasing triplet.
                return True
        return False