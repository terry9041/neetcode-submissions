class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = ["x"] * (amount+1)
        dp[0] = 0
        for val in range(1,amount+1):
            minStep = 10001
            for coin in coins:
                if val-coin >= 0 and dp[val-coin] != "x":
                    minStep = min(minStep, dp[val-coin]+1)
            if minStep != 10001:
                dp[val] = minStep

        return dp[-1] if dp[-1] != "x" else -1

    #    0 1 2 3 4 5 6 7 8 9 10 11 12
    #    0 1 x x x 1 2 3 4 5 1  2  3