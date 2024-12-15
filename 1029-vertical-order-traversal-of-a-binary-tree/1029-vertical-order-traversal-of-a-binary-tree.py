from collections import defaultdict, deque
import heapq


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        # Step 1: Dictionary to store nodes, with x as the key and (y, value) pairs in a list

        node_map = defaultdict(list)

        # Step 2: BFS traversal queue with (node, x, y)
        queue = deque([(root, 0, 0)])

        while queue:
            node,x,y = queue.popleft()
            
            # Add node to the map: store (y, value) for sorting
            heapq.heappush(node_map[x],(y,node.val))

            #add children to the queue with updated x and y
            if node.left:
                queue.append([node.left, x-1, y+1])
            if node.right:
                queue.append([node.right, x+1, y+1])
        

        # Step 3: Sort by x (vertical line) and extract sorted (y, value) nodes
        result = []
        for x in sorted(node_map.keys()):
            column = []
            while node_map[x]:
                column.append(heapq.heappop(node_map[x])[1])
            result.append(column)

        return result
