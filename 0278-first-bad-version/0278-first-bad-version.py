# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Time Complexity : O(log(n))
        # Space Complexity: O(1)
        left, right = 0, n

        while left<right:
            mid = (left + right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        
        return left


# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         # Time Complexity : O(n)
#         # Space Complexity: O(1)
#         for i in range(1,n+1):
#             if isBadVersion(i):
#                 return i
#             continue
        
#         return -1


        