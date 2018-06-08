class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        buy, sell, cool = [0] * 2, [0] * 2, [0] * 2
        buy[0] = -prices[0]
        for i in range(1, len(prices)):
            buy[i % 2] = max(buy[(i - 1) % 2], cool[(i - 1) % 2] - prices[i])
            sell[i % 2] = buy[(i - 1) % 2] + prices[i]
            cool[i % 2] = max(sell[(i - 1) % 2], cool[(i - 1) % 2])
        return max(cool[(len(prices) - 1) % 2], sell[(len(prices) - 1) % 2])
        
        
