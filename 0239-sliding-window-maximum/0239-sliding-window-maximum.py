from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for i, num in enumerate(nums):
            # check for out of window elements
            if dq and dq[0] == i-k:
                dq.popleft()
            
            # while the top element is less than the current visiting element pop from last to maintian decreasing queue. 
            while dq and nums[dq[-1]] < num:
                dq.pop()
            
            # Append element in queue at top
            dq.append(i)
            
            # from the kth location start inserting max value which is the start in decreasing array. 
            if i >= k-1:
                res.append(nums[dq[0]])
        
        return res

# If you were to use a brute-force approach, you'd scan each window of size k and compute the max:
# for i in range(len(nums) - k + 1):
#     res.append(max(nums[i:i+k]))

# Time Complexity:
#   Each max() call takes O(k) time.
#   For n elements, you do this n - k + 1 times.
#   Total: O(nk) — which is inefficient for large n and k.

# Time Complexity when deque is used here:
#   Each element is added and removed at most once from the deque.
#   So the entire algorithm runs in O(n) time.

# Space Complexity:
#    The deque holds at most k elements, so O(k) space.