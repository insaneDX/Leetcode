class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        island = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # down, right, up, left


        def dfs(row, col):
            visited.add((row, col))
            for x, y in directions:
                new_row = row + x
                new_col = col + y

                if (new_row in range(rows) and new_col in range(cols) and (new_row, new_col) not in visited 
                    and grid[new_row][new_col] == "1"):
                    dfs(new_row, new_col)

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == "1":
                    island += 1
                    dfs(row, col)

        return island
