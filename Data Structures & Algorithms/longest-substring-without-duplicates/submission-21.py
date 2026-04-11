class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set() # keep track of seen for every pair of lr ptr
        res = 0

        # sliding window
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            res = max(res, r-l+1)
            seen.add(s[r])
        
        return res
            