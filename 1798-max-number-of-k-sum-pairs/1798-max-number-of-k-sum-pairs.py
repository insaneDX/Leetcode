class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #Time Complexity: (N)
        #Space Complexity: (N)
        count = {}
        operations = 0

        for num in nums:
            complement = k - num
            if complement in count and count[complement] > 0:
                operations += 1
                count[complement] -= 1
            else:
                if num in count:
                    count[num] += 1
                else:
                    count[num] = 1
        
        return operations


# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         #Time Complexity: (N^2) for 2 for loops
#         #Space Complexity: (N) for Visited set

#         operations = 0
#         visited = [False] * len(nums)

#         for left in range(len(nums)-1):
#             if visited[left]:  # Skip if already visited
#                 continue
#             for right in range(left + 1, len(nums)):
#                 if (nums[left] + nums[right] == k) and not visited[right]:
#                     operations += 1
#                     visited[left] = True
#                     visited[right] = True
#                     break  # Move to the next 'left' index after finding a pair
        
#         return operations
