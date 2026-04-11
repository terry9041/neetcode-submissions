class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # # TC: O(N)
        # # SC: O(N)
        # if len(cost) == 1:
        #     return 0
        # if len(cost) == 2:
        #     return min(cost[-1], cost[-2])
        # dp = [[] for _ in range(len(cost)+1)]
        # dp[0] = 0
        # dp[1] = 0
        # for i in range(2,len(cost)+1):
        #     cost1 = dp[i-1] + cost[i-1]
        #     cost2 = dp[i-2] + cost[i-2]
        #     dp[i] = min(cost1, cost2)
        # return dp[-1]

        # TC: O(N)
        # SC: O(1)
        if len(cost) == 1:
            return 0
        if len(cost) == 2:
            return min(cost[-1], cost[-2])
        dp1 = cost[1] # dp1 = cost of reaching 2 using ss1
        dp2 = cost[0] # dp2 = cost of reaching 2 using ss2
        for i in range(3,len(cost)+1): # index i is the target
            temp = dp2 # we use prev dp2 for later, so save it
            dp2 = dp1 # min cost of reaching i+1 with ss2 = min cost of reaching i with ss1 
            dp1 = cost[i-1] + min(dp1,temp) # min cost of reaching i+1 with ss1 = cost at i-1 + min cost to reach i-1
        return min(dp1,dp2)

