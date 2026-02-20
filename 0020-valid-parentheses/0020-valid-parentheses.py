class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack = []

        for c in s:
            if c in closeToOpen: # we enconter closing pair
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else: 
                    return False # if stack top element is not the closing pair of current parantheses
            else:
                stack.append(c)
            
        return True if not stack else False
                



        

        