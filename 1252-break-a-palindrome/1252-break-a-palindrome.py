class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # A palindrome with length 1 or less cannot be broken
        if len(palindrome) <= 1:
            return ""
        
        # Convert the string to a list to modify it
        palindrome = list(palindrome)
        n = len(palindrome)
        
        # Try to replace the first non-'a' character in the first half with 'a'
        for i in range(n // 2):
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                # Return the modified palindrome if it's not the same as the original
                return ''.join(palindrome)
        
        # If all characters in the first half are 'a', replace the last character with 'b'
        palindrome[-1] = 'b'
        return ''.join(palindrome)
