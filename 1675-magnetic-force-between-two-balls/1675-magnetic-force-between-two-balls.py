class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Sort the position for using this as a search space
        position.sort()

        # Initial search space
        left, right = 0, position[-1] - position[0]
        
        while left <= right:
            mid = (left + right ) // 2
            if self.can_place_balls(mid, position, m): # if we are able to place m balls with thisthreshold then shrink the search space and search right portion only. 
                answer = mid
                left = mid + 1
            else:
                right = mid - 1 # if unable to place m balls then reduce the threshold and search the left space only.

        return answer

    def can_place_balls(self, x, position, m):
        prev_ball_pos = position[0]
        balls_placed = 1

        # iterate on each position and place there if we can place it
        for i in range(1, len(position)):
            curr_pos = position[i]
            if curr_pos - prev_ball_pos >= x:
                balls_placed += 1
                prev_ball_pos = curr_pos

            if balls_placed == m: # return if m balls are placed with this threshold
                return True
        return False 

# Step 1: Define the search space.
# We're trying to maximize the minimum distance between any two placed balls.
# So our search space ranges from 0 (no distance) to the maximum possible distance between the first and last positions.

# Step 2: Use binary search to find the optimal minimum distance.
# For each midpoint in the search space, we check if it's feasible to place all m balls such that each is at least 'mid' units apart.
# If it's possible, we store that value as a potential answer and try to find a larger one (search right).
# If it's not possible, we reduce the search space (search left).

# Step 3: Placement logic.
# We always place the first ball at the first position.
# Then, for each subsequent position, we check if the distance from the last placed ball is at least 'mid'.
# If yes, we place another ball.
# If we manage to place all m balls this way, the current 'mid' is valid.

# Time Complexity: O(n log d), where n is the number of positions and d is the distance range (position[-1] - position[0]).
# Space Complexity: O(1)