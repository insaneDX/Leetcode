class Solution:

    def calculateHours(self, piles: List[int], speed: int) -> int:
      hours = 0
      for pile in piles:
          hours += (pile + speed - 1) // speed 
      return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1,max(piles)
        while left<right:
          mid = ((left + right) //2) 
          print(left, right)
          
          timetaken = self.calculateHours(piles,mid)
          print(mid, timetaken)
          if timetaken > h: #search right of mid
            left = mid + 1

          else: #search left of mid
            right = mid
          
           
        return left