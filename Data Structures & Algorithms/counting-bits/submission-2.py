class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111 10000
        # 0 1 1  2  1   2   2   3   1    2    2    3    2     3    3    4
        # 0 1 2  3  4   5   6   7   8
        def largestPowerOfTwo(n):
            return 1 << (n.bit_length()-1)
            # eg 8 = 1000 -> 3 -> 1000, 7 = 111 -> 2 -> 100

        if n == 0:
            return [0]
        elif n == 1:
            return [0,1]
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-largestPowerOfTwo(i)] + 1
        return dp



        
        