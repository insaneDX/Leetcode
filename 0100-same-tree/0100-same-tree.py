# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Time Complexity : O(n)
        # Space Complexity : O(h), where h is the height of the tree.
        # In the worst case, the height of the tree could be h=n (in a completely unbalanced tree, like a linked list).

        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        def dfs(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None or p.val != q.val:
                return False

            # Recursively compare the left and right subtrees
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)
            
            # Both left and right subtrees must match
            return left and right

        return dfs(p, q)
