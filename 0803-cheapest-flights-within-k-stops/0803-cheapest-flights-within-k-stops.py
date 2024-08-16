import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))
        
        
        # Min-heap to store (cost, current_node, stops)
        min_heap = [(0, src, 0)]
        # Distance array to store the minimum cost to reach each node with a given number of stops
        distance = [[float('inf')] * (k + 2) for _ in range(n)]
        distance[src][0] = 0
        
        while min_heap:
            curr_cost, node, stops = heapq.heappop(min_heap)
            
            # If we reach the destination and stops <= k, return the cost
            if node == dst:
                print(distance)
                return curr_cost
            
            # If we can still take more stops
            if stops <= k:
                for neighbor, weight in graph[node]:
                    new_cost = curr_cost + weight
                    # If we find a cheaper cost with fewer stops, push to the heap
                    if new_cost < distance[neighbor][stops + 1]:
                        distance[neighbor][stops + 1] = new_cost
                        heapq.heappush(min_heap, (new_cost, neighbor, stops + 1))
        return -1 if distance[dst][k + 1] == float('inf') else distance[dst][k + 1]