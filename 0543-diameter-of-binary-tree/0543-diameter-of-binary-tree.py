# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize the maximum diameter to 0
        self.max_diameter = 0
        
        def dfs(node):
            # Base case: if the node is None, return 0
            if node is None:
                return 0
            
            # Recursively get the depth of the left and right subtrees
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            
            # Update the maximum diameter if the sum of the left and right depths is larger
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            
            # Return the depth of the current node's subtree
            # The depth is the maximum of the left or right subtree depth plus 1 for the current node
            return max(left_depth, right_depth) + 1
        
        # Start the depth-first search from the root
        dfs(root)
        
        # Return the maximum diameter found
        return self.max_diameter
