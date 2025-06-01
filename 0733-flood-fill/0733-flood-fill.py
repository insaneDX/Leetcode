class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        rows, cols = len(image), len(image[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(row, col):
            if not (0 <= row < rows and 0 <= col < cols) or image[row][col] != original_color:
                return
            image[row][col] = color
            for x, y in directions:
                dfs(row + x, col + y)

        if original_color != color:
            dfs(sr, sc)

        return image