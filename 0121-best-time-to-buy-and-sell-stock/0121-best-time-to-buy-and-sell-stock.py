class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_p = float('inf')  # Initialize min_p to a very high value
        max_p = 0
        
        for price in prices:
            if price < min_p:
                min_p = price  # Update min_p if a new lower price is found
            
            current_profit = price - min_p  # Calculate current profit
            if current_profit > max_p:
                max_p = current_profit  # Update max_p if the current profit is greater
        
        return max_p