class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res += (1 & (n >> i)) * (2 ** (31-i))
        return res