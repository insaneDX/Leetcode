class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = min(len(word1), len(word2))
        result = "".join(word1[i] + word2[i] for i in range(length))
        result += word1[length:] + word2[length:]
        return result