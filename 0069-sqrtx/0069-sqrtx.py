class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        # setting search space for binary search problem
        left, right = 1, x // 2  # sqrt(x) will never be more than x // 2 for x >= 2

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right  # right is the floor of sqrt(x)
        