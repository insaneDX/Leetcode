class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        keys = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def dfs(index, path):
            if index == len(digits):
                result.append(path)
                return
            
            for ch in keys[digits[index]]:
                dfs(index+1, path + ch)
        
        dfs(0, "")

        return result


# Time complexity
# Each digit maps to:
# 3 letters → (2,3,4,5,6,8)
# 4 letters → (7,9)
# n = len(digits)
# O(n × 4^n)   (worst case)
# O(n × 3^n)   (average case)

# Space complexity
# O(n × 4^n)   (dominant: result)