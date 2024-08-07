class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #approach perform two binary search on rows and cols

    rows, cols = len(matrix), len(matrix[0])
    top, bot = 0, rows-1 # left pointer to 0 and right pointer to last row
    while top<=bot: # find row column search
      mid_row = (top + bot) // 2
      if target > matrix[mid_row][-1]: # search in next row if last element in the middle row is greater than target
        top = mid_row + 1
      elif target < matrix[mid_row][0]: # search in previous row if 1st element in the middle row is greater than target
        bot = mid_row - 1
      else:   # this is the row where target lies
        break
    
    if(top>bot):
      return False

    row = (top + bot)//2

    l, r = 0, cols-1
    while l<=r:
      mid_col = (l+r)//2
      if target > matrix[row][mid_col]:
        l = mid_col + 1
      elif target < matrix[row][mid_col]:
        r = mid_col - 1
      else:
        return True
    
    return False
