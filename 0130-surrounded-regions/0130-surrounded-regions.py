class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def dfs(m, n):
            if not 0<=m<rows or not 0<=n<cols:
                return 0
            if board[m][n] != "O":
                return
                                
            if board[m][n] == "O":
                board[m][n] = "S"
        
            dfs(m+1, n)
            dfs(m-1, n)
            dfs(m, n+1)
            dfs(m, n-1)


        # set boundary rows and its connected as "Safe"
        # top and bottom rows
        for col in range(cols):
            dfs(0, col)
            dfs(rows-1, col)
        
        # left and right cols
        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols-1)

        # set remaining O to X
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
        
        # Restore safe cells to O
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "S":
                    board[row][col] = "O"

# Time Complexity: O(R * C), Space Complexity: O(R * C) (due to recursion stack and/or visited set)