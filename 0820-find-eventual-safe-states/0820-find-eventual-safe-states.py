class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = [0] * len(graph) # 0 for unvisited, 1 for visited, 2 for safe
        def dfs(state):
            if visited[state] == 1: # if cycle found 
                return False
            if visited[state] == 2: # if a state is already safe(Memoization)
                return True

            visited[state] = 1  # mark current node as visited
            for neighbor in graph[state]:
                if not dfs(neighbor): # if cycle found for neighbor then mark that state as unsafe
                    return False
            
            visited[state] = 2
            return True

        result = []
        # Run DFS on all states
        for state in range(len(graph)):
            if dfs(state): # mark safe state only when all the outgoing path is safe 
                result.append(state)
        
        return result