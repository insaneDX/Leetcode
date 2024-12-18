class Solution:
    def twoCitySchedCost(self, costs):
        # Sort costs based on the difference (cost_A - cost_B)
        costs.sort(key=lambda x: x[0] - x[1])
        
        total_cost = 0
        n = len(costs) // 2  # Number of people to send to each city
        
        # Send first half to City A and second half to City B
        for i in range(n):
            total_cost += costs[i][0]  # Cost of sending to City A
        for i in range(n, 2 * n):
            total_cost += costs[i][1]  # Cost of sending to City B
        
        return total_cost
