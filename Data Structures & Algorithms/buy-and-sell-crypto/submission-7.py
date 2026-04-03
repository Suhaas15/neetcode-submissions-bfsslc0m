class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        max_profit=0
        buy=prices[0]

        for right in range(1, len(prices)):
            if prices[right]<buy:
                buy=prices[right]
                left=right
            
            max_profit = max(max_profit, prices[right]-buy)

        return max_profit
            