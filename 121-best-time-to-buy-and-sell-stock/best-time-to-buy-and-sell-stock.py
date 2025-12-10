class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0
        while buy < len(prices) and sell < len(prices):
            curr_profit = prices[sell] - prices[buy]
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                max_profit = max(curr_profit, max_profit)
            sell += 1
        return max_profit

        