class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_row = len(board)
        len_col = len(board[0])
        
        def dfs(i, j, index):
            if index == len(word):
                return True
            if (i < 0 or i >= len_row or j < 0 or j >= len_col or
                board[i][j] != word[index]):
                return False
            
            # Temporarily mark the cell as visited
            temp = board[i][j]
            board[i][j] = '#'
            
            # Explore all four directions
            found = (dfs(i + 1, j, index + 1) or
                     dfs(i - 1, j, index + 1) or
                     dfs(i, j + 1, index + 1) or
                     dfs(i, j - 1, index + 1))
            
            # Restore the cell's original value
            board[i][j] = temp
            
            return found

        for i in range(len_row):
            for j in range(len_col):
                if board[i][j] == word[0]:  # Start DFS from the cell matching the first letter
                    if dfs(i, j, 0):
                        return True
        
        return False