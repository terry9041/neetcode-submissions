class Solution:
    def longestPalindrome(self, s: str) -> str:
        # BF: TC = O(N^3) to check every substring
        n = len(s)
        maxLen = 0
        maxStr = ""

        for p in range(len(s)):

            # check odd length
            l,r = p,p
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > maxLen:
                    maxLen = r-l+1
                    maxStr = s[l:r+1]
                l -= 1
                r += 1
            
            # check even length
            l,r = p, p+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > maxLen:
                    maxLen = r-l+1
                    maxStr = s[l:r+1]
                l -= 1
                r += 1

        return maxStr

        
