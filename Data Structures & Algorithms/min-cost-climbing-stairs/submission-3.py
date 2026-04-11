class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return 0
        if len(cost) == 2:
            return min(cost[-1], cost[-2])
        dp1 = cost[1]
        dp2 = cost[0]
        for i in range(3,len(cost)+1):
            temp = dp2
            dp2 = dp1
            dp1 = cost[i-1] + min(dp1,temp)
        return min(dp1,dp2)