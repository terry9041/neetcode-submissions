class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for p in range(len(s)):
            # check odd length
            l,r = p,p
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            # check even length
            l,r = p,p+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res