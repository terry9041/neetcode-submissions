class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        holding = [-prices[0]] * n
        sell = [0] * n

        for i in range(1, n):
            holding[i] = max(holding[i-1], sell[i-1]-prices[i])
            sell[i] = max(sell[i-1], holding[i] + prices[i])
        return sell[-1]
