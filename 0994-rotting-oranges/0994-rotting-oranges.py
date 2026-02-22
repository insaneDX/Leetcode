class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        fresh = 0

        def valid(m, n):
            return True if (0<=m<rows and 0<=n<cols) else False


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
        
        time = 0
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while queue and fresh>0:
            levelProcessingLength = len(queue)
            for rotten in range(levelProcessingLength):
                currRow, currCol = queue.popleft()
                for dr, dc in directions:
                    newRow = currRow + dr
                    newCol = currCol + dc
                    if valid(newRow, newCol) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        fresh -= 1
                        queue.append((newRow, newCol))
                
            time += 1
        
        return time if fresh == 0 else -1