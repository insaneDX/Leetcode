class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        def dfs(node,path):
            if node == len(graph)-1: # Base case: if we reach the target node
                 result.append(path.copy())
                 return

            
            for neighbor in graph[node]: # Explore all neighbors
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop() # Backtrack
            
            
        dfs(0, [0])
        return result
        