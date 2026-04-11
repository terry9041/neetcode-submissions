class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        debts = [-prices[0]] * n
        profits = [0] * n

        for i in range(1, n):
            debts[i] = min(abs(debts[i-1]), prices[i]) * -1
            profits[i] = max(profits[i-1], debts[i] + prices[i])
        return profits[-1]
