# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        def dfs(node, curr_sum):
            if not node:
                return 0
            curr_sum += node.val
            # equation: curr_sum : (prefixes + current_node) 
            # equation: curr_sum - target = prefix

            #check if prefix existed?
            count = prefix_sum[curr_sum - targetSum]
            
            # append curr_sum
            prefix_sum[curr_sum] += 1

            # travere left and right node
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            # backtrack and remove prefix_sum to traverse other path
            prefix_sum[curr_sum] -= 1

            return count
        return dfs(root, 0)
            

