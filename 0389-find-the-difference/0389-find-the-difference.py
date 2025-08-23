class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Time complexity: O(N)
        # Space complexity: O(1)

        sum_s = sum(ord(char) for char in s)
        sum_t = sum(ord(char) for char in t)
        
        return chr(sum_t - sum_s)

# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         # Time complexity: O(N log N)
#         # Sorting both strings takes O(N log N) time.
#         # The loop then takes O(N) time. Here sorting dominates the time complexity.
#         # Space complexity: O(N)
#         s_sorted = sorted(s)
#         t_sorted = sorted(t)

#         for i in range(len(s_sorted)):
#             if s_sorted[i] != t_sorted[i]:
#                 return t_sorted[i]
        
#         return t_sorted[-1]

