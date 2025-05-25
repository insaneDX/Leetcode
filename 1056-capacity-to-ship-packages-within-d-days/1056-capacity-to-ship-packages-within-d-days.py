from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Helper function to check if the given capacity is allowed?
        def capacity_check(capacity):
            total_weight = 0  # total weights that can be loaded in a given day
            required_days = 1  # starts with day1
            
            for weight in weights:
                # if adding more weights exceeds the max_capacity allowed
                # move to next ship and increment the day
                if total_weight + weight > capacity:
                    total_weight = 0
                    required_days += 1
                
                total_weight += weight  # load the current weight
            
            # Return True if total days is within allowed day
            return required_days <= days

        # Search space for this binary search algorithm
        # minimum will be the heviest package and maximium can be the sum of all package
        left, right = max(weights), sum(weights)

        # Binary search for the minimum capacity
        while left < right:
            mid = (left + right) // 2  # try the middle capacity
            if capacity_check(mid):
                # If it's possible to ship with this capacity, try smaller
                right = mid
            else:
                # Otherwise, increase capacity
                left = mid + 1
            
        # When loop ends, left is the smallest capacity that is required
        return left
