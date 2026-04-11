class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n < 2:
            return s

        dp = [[False] * n for _ in range(n)]
        
        start_index = 0
        max_len = 1

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and length > max_len:
                    max_len = length
                    start_index = i
        
        return s[start_index:start_index + max_len]

        # TC: O(n^2)
        # SC: O(n^2)

                




