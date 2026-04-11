class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_val = amount + 1
        dp = [max_val] * (max_val)
        dp[0] = 0



        for val in range(1,amount+1):
            minStep = max_val
            for coin in coins:
                if val-coin >= 0 and dp[val-coin] != max_val:
                    minStep = min(minStep, dp[val-coin]+1)
            if minStep != max_val:
                dp[val] = minStep

        return dp[amount] if dp[amount] != max_val else -1

    #    0 1 2 3 4 5 6 7 8 9 10 11 12
    #    0 1 x x x 1 2 3 4 5 1  2  3