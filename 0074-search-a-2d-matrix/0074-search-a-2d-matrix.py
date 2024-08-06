class Solution:

    def helper(self, matrix: List[List[int]], target: int, left, right):
        if left[0] > right[0] or left[1] > right[1]:
            return False

        midx = (left[0] + right[0]) // 2
        midy = (left[1] + right[1]) // 2

        if matrix[midx][midy] == target:
            return True
        elif matrix[midx][midy] > target:
            return self.helper(matrix, target, left, [midx - 1, right[1]]) or \
                   self.helper(matrix, target, [left[0], left[1]], [midx, midy - 1])
        else:
            return self.helper(matrix, target, [midx + 1, left[1]], right) or \
                   self.helper(matrix, target, [left[0], midy + 1], [midx, right[1]])

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        left = [0, 0]
        right = [len(matrix) - 1, len(matrix[0]) - 1]
        return self.helper(matrix, target, left, right)