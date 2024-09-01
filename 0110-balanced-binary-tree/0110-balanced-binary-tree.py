# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True  # An empty tree is balanced
        
        self.balance = True  # Assume the tree is balanced initially
        
        def dfs(node, height):
            if node is None:
                return height  # Return the current height if the node is None
            
            # Recursively calculate the height of the left and right subtrees
            left = dfs(node.left, height + 1)
            right = dfs(node.right, height + 1)
            
            # If the height difference between the left and right subtrees is more than 1, mark as unbalanced
            if abs(left - right) > 1:
                self.balance = False
            
            # Return the height of the current subtree
            return max(left, right)
        
        # Start the DFS from the root node
        dfs(root, 0)
        
        # Return whether the tree is balanced
        return self.balance
