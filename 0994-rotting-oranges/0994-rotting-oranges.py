class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        fresh = 0

        # Helper to check bounds
        def valid(m, n):
            return 0 <= m < rows and 0 <= n < cols

        # Count fresh oranges and enqueue all rotten ones (multi-source BFS start)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))
        
        time = 0
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        # BFS level-by-level (each level = 1 minute)
        while queue and fresh > 0:
            levelProcessingLength = len(queue)

            for _ in range(levelProcessingLength):
                currRow, currCol = queue.popleft()

                for dr, dc in directions:
                    newRow = currRow + dr
                    newCol = currCol + dc

                    # If adjacent cell is fresh, rot it
                    if valid(newRow, newCol) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2   # mark as rotten
                        fresh -= 1
                        queue.append((newRow, newCol))
            
            time += 1  # increment time after one full level (one minute)

        # If no fresh oranges left, return time; otherwise impossible
        return time if fresh == 0 else -1


# Time Complexity: O(R * C)
# We scan the grid once.
# Each cell is processed at most once in BFS.

# Space Complexity: O(R * C)
# In worst case, queue may contain all cells.
# No extra visited matrix (grid modified in-place).