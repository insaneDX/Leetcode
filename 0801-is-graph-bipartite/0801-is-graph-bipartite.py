class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color_group = [0] * n # 0 = unvisited, 1 = red, -1 = blue

        def dfs(node, color):
            color_group[node] = color

            for neighbor in graph[node]:
                if color_group[neighbor] == color:
                    return False
                if color_group[neighbor] == 0:
                    if not dfs(neighbor, -color):
                        return False
            return True 

        for i in range(n):
            if color_group[i]==0:
                if not dfs(i, 1):
                    return False
        
        return True