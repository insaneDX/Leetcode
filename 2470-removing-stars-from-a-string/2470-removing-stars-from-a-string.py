class Solution:
    def removeStars(self, s: str) -> str:
        if len(s)<0:
            return ""
        stack = []
        for char in s:
            if char == "*" and stack:
                stack.pop()
            elif char != "*":
                stack.append(char)
        
        return "".join(char for char in stack)
