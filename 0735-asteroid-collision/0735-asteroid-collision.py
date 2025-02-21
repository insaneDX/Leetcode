class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack


# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         dir = ""
#         stack = []

#         for i in range(len(asteroids)):
#             if asteroids[i] >= 0 and (dir == "" or dir == "+"):
#                 dir = "+"
#                 stack.append(asteroids[i])
#             elif asteroids[i] < 0 and (dir == "" or dir == "-"):
#                 dir = "-"
#                 stack.append(asteroids[i])
            
#             elif asteroids[i] < 0 and dir == "+":
#                 while stack and asteroids[i] < 0 and stack[-1] > 0:
#                     if abs(asteroids[i]) > stack[-1]:
#                         stack.pop()
#                     elif abs(asteroids[i]) == stack[-1]:
#                         stack.pop()
#                         break
#                     else:
#                         break
#                 else:
#                     stack.append(asteroids[i])
#                     dir = "-"
                
#             elif asteroids[i] > 0 and dir == "-":
#                 while stack and asteroids[i] > 0 and stack[-1] < 0:
#                     if abs(asteroids[i]) > abs(stack[-1]):
#                         stack.pop()
#                     elif abs(asteroids[i]) == abs(stack[-1]):
#                         stack.pop()
#                         break
#                     else:
#                         break
#                 else:
#                     stack.append(asteroids[i])
#                     dir = "+"
        
#         return stack

# First approach is correct according to the problem definition on LeetCode, as it ensures only the top element will collide and potentially explode when a new element is inserted, leaving the rest intact. However, my second approach traverses through the stack and causes collisions with every previous element until the conditions are met, which is less efficient.