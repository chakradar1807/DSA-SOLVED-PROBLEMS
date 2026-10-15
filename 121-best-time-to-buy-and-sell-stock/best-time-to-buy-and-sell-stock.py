class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumProfit = 0
        minStockVal = float('inf')
        
        for price in prices:
            if price < minStockVal:
                minStockVal = price
            
            current_profit = price - minStockVal
            
            if current_profit > maximumProfit:
                maximumProfit = current_profit
                
        return maximumProfit