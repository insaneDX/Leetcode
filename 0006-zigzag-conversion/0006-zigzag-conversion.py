class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If the number of rows is 1, return the original string as no conversion is needed
        if numRows == 1:
            return s
        
        # Create an array to hold the rows
        rows = [''] * numRows
        
        # Variable to track the current row we are appending characters to
        curr_row = 0
        
        # Variable to track the direction of movement (1 for moving down, -1 for moving up)
        direction = 1
        
        # Iterate through each character in the string
        for char in s:
            # Append the character to the current row
            rows[curr_row] += char
            
            # If we reach the top row, change direction to move down
            if curr_row == 0:
                direction = 1
            # If we reach the bottom row, change direction to move up
            elif curr_row == numRows - 1:
                direction = -1
            
            curr_row += direction
        
        # Join all rows to form the final converted string
        return ''.join(rows)
