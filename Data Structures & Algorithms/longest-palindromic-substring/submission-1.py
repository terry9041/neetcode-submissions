class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        maxStr = ""

        
        for x in range(len(s)):

            # odd length
            i = j = x
            while i >= 0 and j <= len(s) - 1 and s[i] == s[j]:
                if (j-i+1) > maxLen:
                    maxStr = s[i:j+1]
                    maxLen = j-i+1
                i -= 1
                j += 1
        
            # even length
            i, j = x, x + 1
            while i >= 0 and j <= len(s) - 1 and s[i] == s[j]:
                if (j-i+1) > maxLen:
                    maxStr = s[i:j+1]
                    maxLen = j-i+1
                i -= 1
                j += 1

        return maxStr 

                