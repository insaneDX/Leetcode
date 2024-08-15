class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:    
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # down, right, up, left
        island = 0

        def bfs(row, col):
            queue = collections.deque()
            visited.add((row, col))
            queue.append((row, col))

            while queue:
                current_row, current_col = queue.popleft()
                for x, y in directions:
                    new_row = current_row + x
                    new_col = current_col + y

                    if (new_row in range(rows) and new_col in range(cols) and (new_row, new_col) not in visited) and grid[new_row][new_col] == "1":
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == "1":
                    bfs(row, col)
                    island += 1

        return island