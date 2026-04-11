class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111 10000
# res     0 1 1  2  1   2   2   3   1    2    2    3    2     3    3    4
# num     0 1 2  3  4   5   6   7   8
# offset  1 1 2  2  4   4   4   4   8
        def largestPowerOfTwo(n):
            return 1 << (n.bit_length()-1)
            # eg 8 = 1000 -> 3 -> 1000, 7 = 111 -> 2 -> 100

        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = dp[i-offset] + 1
        return dp


        
        