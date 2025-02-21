class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        from collections import Counter

        # Count frequencies of characters in each word
        word1_counter = Counter(word1)
        word2_counter = Counter(word2)
        
        # Check if they have unique characters
        if set(word1_counter.keys()) != set(word2_counter.keys()):
            return False
        
        # Check if both words have the same frequencies (ignoring character order)
        if sorted(word1_counter.values()) != sorted(word2_counter.values()):
            return False
        
        return True

# Approach 
# 1. Characters between two words should be common and length should be same
# 2. check for frequency aab can be converted to bba but aaab, cannot be converted to bbba. No amount of swapping can change the frequencies to make these two strings identical.
