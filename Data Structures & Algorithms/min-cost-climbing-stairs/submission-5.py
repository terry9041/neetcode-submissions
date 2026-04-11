class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # TC: O(N)
        # SC: O(1)
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return 0
        if len(cost) == 2:
            return min(cost[-1], cost[-2])
        # SC: O(N)
        n = len(cost)
        dp = [[] for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 0
        dp[2] = min(cost[0], cost[1])
        for i in range(3,n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[-1]

        # # SC: O(1)
        # dp1 = cost[1]
        # dp2 = cost[0]
        # for i in range(3,len(cost)+1):
        #     temp = dp2
        #     dp2 = dp1
        #     dp1 = cost[i-1] + min(dp1,temp)
        # return min(dp1,dp2)

