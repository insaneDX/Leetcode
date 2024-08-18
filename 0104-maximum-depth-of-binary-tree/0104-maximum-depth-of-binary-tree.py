class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_count = 0
        def dfs(node, count):
            nonlocal max_count  # Add this line Without nonlocal: The inner function would create a new local variable x, 
                                # and the outer variable x would remain unchanged.
                                # With nonlocal: The inner function modifies the variable x in the outer function.

            if node is None:
                max_count = max(max_count, count)
                return
            dfs(node.left, count + 1)
            dfs(node.right, count + 1)

        dfs(root, 0)
        return max_count

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         def dfs(node, count):
            
#             if node == None:
#                 return count
#             left = node.left 
#             right = node.right
#             left_depth = dfs(left, count + 1)
#             right_depth = dfs(right, count + 1)
#             return max(left_depth, right_depth)

#         return dfs(root,0)
