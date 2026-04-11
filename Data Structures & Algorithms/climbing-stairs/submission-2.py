class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        ways = [[] for _ in range(n+1)]
        ways[0] = 0
        ways[1] = 1
        ways[2] = 2
        for i in range(3,n+1):
            ways[i] = ways[i-1] + ways[i-2]
        return ways[n]