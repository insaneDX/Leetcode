class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_island = 0
        directions = [[0,1], [1,0], [-1,0], [0,-1]]

        def dfs(row, col):
            if (row < 0 or row >= rows) or (col < 0 or col >= cols) or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            area = 1
            # Add the area of each direction
            area += (
                dfs(row + 1, col) +
                dfs(row - 1, col) +
                dfs(row, col + 1) +
                dfs(row, col - 1)
            )
            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_island = max(max_island, dfs(row, col))

        return max_island