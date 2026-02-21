class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # stop if out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            # stop if water
            if grid[r][c] == 0:
                return
            
            # mark this land as safe (convert to water)
            grid[r][c] = 0

            # explore 4 directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        
        # Remove all land connected to boundary

        # top and bottom rows
        for col in range(cols):
            dfs(0, col)
            dfs(rows-1, col)

        # left and right columns
        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols-1)

        # 2Count remaining land (these are enclaves)
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count += 1

        return count