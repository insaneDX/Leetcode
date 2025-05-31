from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited = set()

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Helper to check if (row, col) is within bounds
        def isValid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        # DFS to mark all land cells of the first island
        def dfs(row, col):
            if not isValid(row, col) or (row, col) in visited or grid[row][col] != 1:
                return
            visited.add((row, col))
            for x, y in directions:
                new_row, new_col = row + x, col + y
                dfs(new_row, new_col)

        # BFS to expand from the first island and find the shortest bridge to the second
        def bfs():
            res = 0
            q = deque(visited)  
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    for x, y in directions:
                        new_row, new_col = row + x, col + y
                        # Skip if out of bounds or already visited
                        if not isValid(new_row, new_col) or (new_row, new_col) in visited:
                            continue
                        # If we reach a land cell of the second island, return steps taken to reach
                        if grid[new_row][new_col] == 1:
                            return res
                        # Else, add water cell to the queue and continue BFS
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))
                res += 1
            return res

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(row, col)  
                    return bfs()   


# Time Complexity: O(n * m)
# Space Compexity: O(n * m)
