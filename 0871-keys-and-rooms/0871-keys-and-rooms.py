class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0] * len(rooms)  # 0 for unvisited, 1 for visited

        def dfs(room):
            visited[room] = 1  # Mark as visited
            for neighbor in rooms[room]:  # Visit all neighbors
                if visited[neighbor] == 0:
                    dfs(neighbor)

        dfs(0)  # Start DFS from room 0

        return all(visited)  # If all rooms were visited, return True