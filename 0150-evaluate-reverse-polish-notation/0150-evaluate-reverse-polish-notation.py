from typing import List
class Solution:

    def validNum(self,str):
      try: 
        int(str)
        return True
      except:
        return False

    def evalRPN(self, tokens: List[str]) -> int:
      self.stack = []
      for i in range(len(tokens)):
        if self.validNum(tokens[i]):
          self.stack.append(tokens[i])
        else:
          a = int(self.stack.pop())
          b = int(self.stack.pop())
          if tokens[i] == "/":
            c = b / a
            self.stack.append(c)
          if tokens[i] == "*":
            c = b * a
            self.stack.append(c)
          if tokens[i] == "+":
            c = b + a
            self.stack.append(c)
          if tokens[i] == "-":
            c = b - a
            self.stack.append(c)

      return int(self.stack[0])