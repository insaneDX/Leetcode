class Solution:
    def matchup(self,a,b):
        if a == '{' and b == '}':
            return True
        if a == '[' and b == ']':
            return True
        if a == '(' and b == ')':
            return True
  
        return False
    def isValid(self, s: str) -> bool:
        stack = []
        top = -1
        valid = False

        for char in s:
            if top >= 0 and self.matchup(stack[top],char):
                stack.pop()
                valid = True
                top -= 1
            else :
                top +=  1
                stack.append(char)
                valid = False

  
        if len(stack) == 0:
            return valid
        else: 
            return False

        