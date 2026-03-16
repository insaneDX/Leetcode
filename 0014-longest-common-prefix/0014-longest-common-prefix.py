class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""

        min_len = min(len(word) for word in strs)
        for i in range(0, min_len):
            char = strs[0][i]

            for word in strs:
                if char != word[i]:
                    return prefix
            
            prefix += char
        
        return prefix