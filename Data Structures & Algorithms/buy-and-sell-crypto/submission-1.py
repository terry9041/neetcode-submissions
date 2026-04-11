class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        debts = [101] * n
        profits = [101] * n

        debts[0], profits[0] = -prices[0], 0
        for i in range(1, n):
            debts[i] = min(abs(debts[i-1]), prices[i]) * -1
            profits[i] = max(profits[i-1], debts[i] + prices[i])
        return profits[-1]
