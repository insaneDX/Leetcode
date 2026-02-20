# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        
        result = []
        q = collections.deque()
        q.append(root)

        while q:
            q_len = len(q)  # extract the queue size as it is dynamic queue, childs will be appended
            level = []  # list to store level elements
            for i in range(q_len):  # process each element and append their children
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)

        return result