class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 1:
            return 0
        Left = 0
        Right = len(height) - 1
  
        maxCC = 0

        while Left<Right:
            maxCC = max(maxCC, min(height[Left],height[Right]) * (Right - Left))
            if height[Left] < height[Right]:
                Left += 1
            else:
                Right -= 1
        return maxCC
        