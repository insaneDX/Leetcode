class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(n):
            while s[right] in char_set: # If the current character is already in the set, remove the leftmost character until all characters are unique
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length
