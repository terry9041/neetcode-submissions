class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        curr_fuel = 0
        res_idx = 0
        for i in range(len(gas)):
            curr_fuel += gas[i]
            curr_fuel -= cost[i]
            if curr_fuel < 0:
                curr_fuel = 0
                res_idx = i + 1
        return res_idx