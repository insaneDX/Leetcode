class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
      sub_set = []

      for i in range(n):
        sums = nums[i]
        sub_set.append(sums)
        for j in range(i+1,n):
          sums += nums[j]
          sub_set.append(sums)
          
        
      
      sub_set.sort()

      total = sum(sub_set[left-1:right])


      return total % 1000000007