from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length = 0
        odd_found = False
        for freq in count.values():
            # Add the largest even number of characters we can use
            # Example: "aaaa" (freq=4) → add all 4
            #          "aaaaa" (freq=5) → add 4 (leave 1 out for now)
            length += (freq // 2) * 2  
            
            # If there's an odd count, remember that we can place
            # exactly one odd character in the middle of the palindrome
            if freq % 2 == 1:
                odd_found = True

        # If any odd was found, add 1 for the center character
        return length + 1 if odd_found else length
