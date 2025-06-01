class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        pixel_color = image[sr][sc]
        

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def isValid(row, col):
            return 0<=row<len(image) and 0<=col<len(image[0])
        
        def dfs(row, col):
            if not isValid(row, col) or image[row][col] != pixel_color or image[row][col] == color:
                print(row, col)
                return
            image[row][col] = color

            for x, y in directions:
                dfs(row + x, col + y)
            


        dfs(sr, sc)
        return image
        