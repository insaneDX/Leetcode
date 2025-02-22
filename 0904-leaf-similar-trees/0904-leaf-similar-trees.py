# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def traverse(node, data):
            if node:
                if not node.left and not node.right:  # It's a leaf node
                    data.append(node.val)
                traverse(node.left, data)
                traverse(node.right, data)
            return data
        
        data1 = traverse(root1, [])
        data2 = traverse(root2, [])                
        
        return data1 == data2
