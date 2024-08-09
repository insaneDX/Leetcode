class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        result = []
        self.helper(path, 0, n, result,1,k)
        return result

        return result
    def helper(self, path, curr_sum, target, result,start,max_length):
        if curr_sum > target or len(path) > max_length:
            return
        if curr_sum == target and len(path) == max_length:
            result.append(path[:])
        
        for i in range(start, 10): # choose
            path.append(i)
            self.helper(path, curr_sum + i,target, result,i+1,max_length)
            path.pop()
