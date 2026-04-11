class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = set()

        l = 0
        for r in range(len(s)):
            # increment L if needed to create valid window
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            # only then we update max and put R into seen
            res = max(res, r-l+1)
            seen.add(s[r])
        
        return res