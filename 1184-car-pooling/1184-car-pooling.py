class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0]*1001 # Constraint 1 <= trips.length <= 1000

        for passengers, start, end in trips:
            diff[start] += passengers
            diff[end] -= passengers
        
        passengers_count = 0
        for passengers in diff:
            passengers_count += passengers
            if passengers_count > capacity:
                return False
        
        return True

# Time Complexity: O(N + M) - O(N) for iterating over trips, O(M) for iterating over the diff array, where M = 1001
# Space Complexity: O(M)